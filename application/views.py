from django.shortcuts import render
from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
# Create your views here.

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
