#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import Booking  # Import the Booking model
from .models import Menu

class UserSerializer(serializers.ModelSerializer):

 class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields from the Booking model
