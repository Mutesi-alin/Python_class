from django.shortcuts import render
from .serializers import studentSerializer
from rest_framework.response import Response
from student.models import Student
from rest_framework.views import APIView

# Create your views here.
class studentListView(APIView):
        def get (self,request):
                students= Student.objects.all()
                serialize= studentSerializer(students,many=True)
                return Response (serialize.data)



