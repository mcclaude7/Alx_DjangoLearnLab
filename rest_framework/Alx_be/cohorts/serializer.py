from rest_framework import serializers
from .models import Cohort

class CohortSerializer(serializers.ModelSerializer):
    name = Cohort
    field = '__all__'