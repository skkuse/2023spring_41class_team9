from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)


