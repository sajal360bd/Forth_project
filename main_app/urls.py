
from django.urls import path
from .views import *

urlpatterns = [
   path('',index,name='index_page'),
   path('about',about,name='about'),
   path('contact',contact,name='contact'),
   path('properties',properties,name='properties'),
   path('property-single',property_single,name='property-single'),
   path('services',services,name='services'),
   
]