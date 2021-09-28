from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',UserAPI, basename='RegisterUser')
router.register('user_register', RegisterAPI, basename='User_register')
router.register('profile', ProfileAPI, basename='profile')
router.register('vital', VitalAPI),
router.register('social_history', SocialHistoryAPI),
router.register('surgery', SurgeryAPI)


urlpatterns = [
    path('', include(router.urls)),
]
