from django.db import models
import jsonfield
# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class user_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data')
    Relation_name = models.CharField(max_length=50, null=True, blank=True)
    Relationship = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    dob = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    bmi = models.CharField(max_length=50, null=True, blank=True)
    ethnicity = models.CharField(max_length=50, null=True, blank=True)
    disability = jsonfield.JSONField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    hip_circum = models.CharField(max_length=50, null=True, blank=True)
    waist_circum = models.CharField(max_length=50, null=True, blank=True)
    whr = models.CharField(max_length=50, null=True, blank=True)
    alcohol = jsonfield.JSONField(null=True, blank=True)
    coffee = jsonfield.JSONField(null=True, blank=True)
    sexual_orientation = jsonfield.JSONField(null=True, blank=True)
    tobacco = jsonfield.JSONField(null=True, blank=True)
    other = jsonfield.JSONField(null=True, blank=True)
    surgery = jsonfield.JSONField(null=True, blank=True)


# class vitals(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
#     hip_circum = models.CharField(max_length=50, null=True, blank=True)
#     waist_circum = models.CharField(max_length=50, null=True, blank=True)
#     whr = models.CharField(max_length=50, null=True, blank=True)


class education(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name='education_profile')
    year_of_education = models.CharField(max_length=50, null=True, blank=True)
    employee_status = models.CharField(max_length=50, null=True, blank=True)
    occupation = jsonfield.JSONField(null=True, blank = True)

class sexual(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name='sexual_profile')
    abusement = models.CharField(max_length=50, null=True, blank=True)
    abusement_status = jsonfield.JSONField(null = True, blank = True)
    sexual_status = jsonfield.JSONField(null=True, blank = True)

class caffine(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name='caffine_profile')
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)


class Tobacco(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name='tobacco_profile')
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)


class Alchol(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name="alchol_profile")
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)

class Other(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True,null=True, related_name="other_profile")
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)



    


    