
from django.urls import path
from .views import *
urlpatterns = [
    
    path('',index),
    path('services/',services),
    path('contact/',contact),
    path('pricing/',pricing),
    path('about/',about),
]