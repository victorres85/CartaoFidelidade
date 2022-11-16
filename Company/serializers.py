from rest_framework import serializers
from .models import Companies, Cards, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
class CompaniesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= Companies
        fields = ('id', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'phone_number')

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'company', 'description', 'total_points')