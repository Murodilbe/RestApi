from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Category, Cars
from App.serializers import CarsSerializer

# Create your views here.

class CarsApiView(ListAPIView):
    queryset = Cars.objects.filter(published=True)
    serializer_class = CarsSerializer

class CarsDetail(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
