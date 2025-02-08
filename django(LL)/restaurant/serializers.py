#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import Booking  # Import the Booking model

class UserSerializer(serializers.ModelSerializer):

 class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields from the Booking model
