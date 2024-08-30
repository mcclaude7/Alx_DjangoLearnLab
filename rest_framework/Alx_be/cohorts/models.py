from django.db import models

# Create your models here
class Cohort(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    tag = models.CharField(max_length=5, null=True, blank=True)