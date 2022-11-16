from django.contrib import admin
from .models import Companies, Cards, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Companies)
admin.site.register(Cards)
admin.site.register(Profile)