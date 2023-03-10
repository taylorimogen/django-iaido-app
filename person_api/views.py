from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from .serializers import PersonSerializer, PersonRestrictedSerializer, UserSerializer
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .view_helpers.person import get_filtered_queryset

# Create your views here.

class PersonView(APIView, LimitOffsetPagination):
    # only admin users have permission to interact with Person API
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get(self, request, username=None):
        """Return a list of paginated Person entities"""
        # if username is entered in URL, return details for that instance of Person only
        if username:
            item = Person.objects.get(username=username)
            serializer = PersonSerializer(item)
            return Response({"message": "Person with username {} has been successfully returned".format(username), "data": serializer.data}, status=status.HTTP_200_OK)

        # if no username is entered, return all instances of Person in response, with optional filtering
        filtered_queryset = get_filtered_queryset(request)
        results = self.paginate_queryset(filtered_queryset, request, view=self)
        serializer = PersonSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):
        """Create new instance of Person"""
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            # creates new instance of Person
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username=None):
        """Update info of person with given username"""
        item = Person.objects.get(username=username)
        serializer = PersonSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            # saves update to instance of Person
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, username=None):
        """Remove instance of Person with given username from the database"""
        item = get_object_or_404(Person, username=username)
        item.delete()
        return Response({"message": "Person with username {} deleted".format(username)}, status=status.HTTP_200_OK)


class PersonRestrictedView(APIView, LimitOffsetPagination):
    # admin and non-admin users can access this endpoint
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Return a list of paginated Person entities,
        accessible to any user and with hidden username and password"""
        filtered_queryset = get_filtered_queryset(request)
        # paginate response using default number of items per page (3)
        results = self.paginate_queryset(filtered_queryset, request, view=self)
        serializer = PersonRestrictedSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)


class UserCreate(generics.CreateAPIView):
    # register a new user
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

