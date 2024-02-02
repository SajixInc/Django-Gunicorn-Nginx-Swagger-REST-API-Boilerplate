from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class homemodel(models.Model):
    Username= models.CharField(max_length=25,unique=True)

    password = models.CharField( max_length=30)
    designation = models.CharField(max_length=5)
    objects = models.Manager

    class Meta:
        db_table = 'api_cosole_users'
