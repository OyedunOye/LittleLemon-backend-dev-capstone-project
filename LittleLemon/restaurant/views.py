from django.shortcuts import render
from rest_framework import generics, viewsets
# from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from .models import Booking, Menu
from .forms import BookingForm
from .serializers import MenuSerializer, BookingSerializer
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# POST and GET view for menu using generic view
class MenuItemView(generics.ListCreateAPIView, TemplateView):
    queryset = Menu.objects.all().order_by('title')
    serializer_class = MenuSerializer
    template_name = 'menu.html'
    context_object_name = "menu_list"

# GET, PUT & DELETE view for each menu record
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# 
class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def list(self, request):
        queryset = Booking.objects.all()
        data = BookingSerializer(queryset)
        # return render(request, 'book.html', {'data':data})
        