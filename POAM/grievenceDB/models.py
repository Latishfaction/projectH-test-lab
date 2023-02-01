from django.db import models

# Create your models here.
class grievence(models.Model):
    property_no = models.IntegerField()
    #concern department
    dept = models.CharField()
    description = models.TextField()
