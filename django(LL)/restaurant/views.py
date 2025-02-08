from django.shortcuts import render
# Create your views here.  
from rest_framework import generics  
from .models import Menu  
from .serializers import UserSerializer  
from rest_framework import viewsets
from .models import Booking  # Import the Booking model
from .serializers import BookingSerializer  # Import the BookingSerializer

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer
