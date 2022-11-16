from django.shortcuts import render
from .serializers import CompaniesSerializer, CardsSerializer, UserSerializer, ProfileSerializer
from .models import Companies, Cards, Profile
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.


class CompaniesViewSet(ModelViewSet):
    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class CardsViewSet(ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Cards.objects.all()  

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()  

    