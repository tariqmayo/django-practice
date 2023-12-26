from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    program = models.CharField(max_length=100)
    is_adult = models.BooleanField()
    email = models.EmailField()
    image = models.ImageField(upload_to="images",  default='user_default.jpg', null=True, blank=True)

