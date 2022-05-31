from django.shortcuts import render
from .serializers import RamenCornerSerializer 
from rest_framework import viewsets      
from .models import RamenCorner                 

class RamenCornerView(viewsets.ModelViewSet):  
    serializer_class = RamenCornerSerializer   
    queryset = RamenCorner.objects.all()   