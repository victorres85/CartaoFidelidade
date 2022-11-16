from django.urls import path, include
from . import viewset
from rest_framework import routers


app_name = 'Business'

router = routers.SimpleRouter()
router.register(r'profiles', viewset.ProfileViewSet, basename='profile_list')
router.register(r'companies', viewset.CompaniesViewSet, basename='company_list')
router.register(r'users', viewset.UserViewSet, basename='user_list')
router.register(r'cards', viewset.CardsViewSet, basename='cards_detail')


urlpatterns = [
    path('', include(router.urls)),
   
]