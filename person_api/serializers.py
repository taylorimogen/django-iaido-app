from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User



class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'age', 'username', 'password')


class PersonRestrictedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'age')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
