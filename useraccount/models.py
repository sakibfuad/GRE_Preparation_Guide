

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    test_no = models.IntegerField( default=0)
    score_point = models.IntegerField( default=0)

