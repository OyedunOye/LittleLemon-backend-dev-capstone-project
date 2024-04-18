from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # define URL pattern for index()
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    # djoser needed to for the below url to function.
    path('api-token-auth/', obtain_auth_token),
]
