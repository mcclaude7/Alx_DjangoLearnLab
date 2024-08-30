from django.shortcuts import render
from .models import Cohort
from rest_framework import viewsets
from .serializer import CohortSerializer
from rest_framework.response import Response


class CohortViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Cohort.objects.all()
        serializer = CohortSerializer(queryset, many=True)
        return Response(serializer.data)
    
def retrieve(self, request, pk=None):
    queryset = Cohort.objects.filter(pk=pk)
    serializer = CohortSerializer(queryset)
    return Response(serializer.data)
    
def create(self, request):
    queryset = Cohort.objects.create(**request.data)
    serializer = CohortSerializer(queryset)
    return Response(serializer.data)