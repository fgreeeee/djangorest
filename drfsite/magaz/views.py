from rest_framework import generics
from django.shortcuts import render
from .models import Magaz
from .serializers import MagazSerializer


class MagazAPIView(generics.ListAPIView):
    queryset = Magaz.objects.all()
    serializer_class = MagazSerializer
