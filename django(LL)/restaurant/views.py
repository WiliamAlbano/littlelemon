from django.shortcuts import render
# Create your views here.  
from rest_framework import generics  
from .models import Menu  
from .serializers import UserSerializer  
from rest_framework import viewsets
from .models import Booking  # Import the Booking model
from .serializers import BookingSerializer  # Import the BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#auth response 
class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})

#imagem html    
def index(request):
    return render(request, 'index.html', {})

#mesas, registros..
class MenuItemsView(generics.ListCreateAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer
