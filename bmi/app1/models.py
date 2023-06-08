from django.db import models

# Create your models here.
class Userdata(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bmi_result = models.CharField(max_length=10)