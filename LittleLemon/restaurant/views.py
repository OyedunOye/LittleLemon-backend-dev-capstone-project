from django.shortcuts import render
from rest_framework import generics, viewsets
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index2.html', {})

# POST and GET view for menu using generic view
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# GET, PUT & DELETE view for each menu record
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# 
class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer