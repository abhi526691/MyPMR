from collections import defaultdict
from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','username', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_data
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    disability = serializers.JSONField()
    class Meta:
        model = Profile
        fields = '__all__'

class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','Relation_name','Relationship', 'height', 'weight', 'bmi', 'hip_circum', 'waist_circum', 'whr']

class SocialHistorySerializer(serializers.ModelSerializer):
    alcohol = serializers.JSONField()
    coffee = serializers.JSONField()
    sexual_orientation = serializers.JSONField()
    tobacco = serializers.JSONField()
    other = serializers.JSONField()  
    class Meta:
        model = Profile
        fields = ['id', 'Relation_name','Relationship', 'alcohol', 'coffee', 'sexual_orientation', 'tobacco', 'other']


class SurgerySerializer(serializers.ModelSerializer):
    surgery = serializers.JSONField() 
    class Meta:
        model = Profile
        fields = ['id', 'Relation_name','Relationship', 'surgery']






