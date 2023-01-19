from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from .serializers import PersonSerializer
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PersonView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username=None):
        """List the details of a given user"""
        if username:
            item = Person.objects.get(username=username)
            serializer = PersonSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        items = Person.objects.all()
        serializer = PersonSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            # creates new instance of Person
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username=None):
        item = Person.objects.get(username=username)
        serializer = PersonSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, username=None):
        item = get_object_or_404(Person, username=username)
        item.delete()
        return Response({"status":"success", "data": "Person with username {} deleted".format(username)})
