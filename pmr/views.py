from django.contrib.auth import authenticate
from django.db.models import query
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, status 
from rest_framework.views import APIView
from .models import Profile, user_data, User
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import models
from rest_framework import viewsets
from rest_framework.permissions import *


def refresh_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }

class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')
        try:
            user = authenticate(request, username = email, password = password)
            if user:
                token = refresh_token(user)
                return Response({"output" : "Logged In Successfully","id" : user.id, 'access_token' : token['access'], 'refresh' : token['refresh']}, status=status.HTTP_202_ACCEPTED)
            return Response({"output" : "Login Failed"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"output" : "Email or Password didn't match"}, status=status.HTTP_401_UNAUTHORIZED)


class UserAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            user_obj = User.objects.create(username = serializer.data['username'])
            if user_obj:
                user_obj.set_password(serializer.data['password'])
                user_obj.first_name = serializer.data['first_name']
                user_obj.save()
                return Response({"output" : "Registered Successfully", "data" : serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"output" : "Not Registered"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"output" : "Not Registered"}, status=status.HTTP_401_UNAUTHORIZED)
    # def create(self, request):
    #     serializer = UserSerializer(data = request.data)
    #     if serializer.is_valid():
    #         print(serializer)
    #         user_obj = User.objects.get_or_create(
    #             username = serializer.data['email']
    #         )
    #         if user_obj:
    #             user_obj.set_password(serializer.data['password'])
    #             user_obj.email = serializer.data['email']
    #             user_obj.first_name = serializer.data['first_name']
    #             user_obj.save()

    #             return Response({"output" : "Registered Successfully", "data" : serializer.data}, status=status.HTTP_201_CREATED)
    #         return Response({"output" : "Not Registered"}, status=status.HTTP_401_UNAUTHORIZED)
    #     return Response({"output" : "Not Registered"}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterAPI(viewsets.ModelViewSet):
    queryset = user_data.objects.all()
    serializer_class = RegisterSerializer

class ProfileAPI(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def list(self, request):
        username = request.data.get('user')
        queryset = Profile.objects.filter(user = username)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        queryset = request.data
        serializer = ProfileSerializer(data=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(instance=queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(instance=queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        queryset.delete()
        return Response({"output" : "Deleted Successfully"})

class VitalAPI(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = VitalSerializer

    def list(self, request):
        username = request.data.get('user')
        print(username)
        queryset = Profile.objects.filter(user = username)
        serializer = VitalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def retrieve(self, request, pk = None):
        queryset = Profile.objects.get(id=pk)
        serializer = VitalSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = VitalSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = VitalSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        queryset.delete()
        return Response({"output" : "Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
      
class SocialHistoryAPI(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = SocialHistorySerializer

    def list(self, request):
        username = request.data.get('user')
        queryset = Profile.objects.filter(user = username)
        serializer = SocialHistorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def retrieve(self, request, pk = None):
        queryset = Profile.objects.get(id=pk)
        serializer = SocialHistorySerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = SocialHistorySerializer(instance=queryset, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = SocialHistorySerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)

class SurgeryAPI(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = SurgerySerializer

    def list(self, request):
        username = request.data.get('user')
        queryset = Profile.objects.filter(user = username)
        serializer = SurgerySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def retrieve(self, request, pk = None):
        queryset = Profile.objects.get(id=pk)
        serializer = SurgerySerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = SurgerySerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Profile.objects.get(id=pk)
        serializer = SurgerySerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"output" : "Updated Successfully"}, status=status.HTTP_202_ACCEPTED)

        return Response({"output" : "Wrongly Entered Data"}, status=status.HTTP_400_BAD_REQUEST)


