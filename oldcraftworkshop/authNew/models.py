from django.db import models

# Create your models here.
class Token(models.Model):
    token = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=6)
    email = models.EmailField()