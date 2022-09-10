from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializers


# Create your views here.
class PersonViewsets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
