from django.shortcuts import render
# Create your views here.  
from rest_framework import generics  
from .models import Menu  
from .serializers import UserSerializer  

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):  
    queryset = Menu.objects.all()  
    serializer_class = UserSerializer  
