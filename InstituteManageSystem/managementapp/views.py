from django.shortcuts import render
from rest_framework.views import APIView
from .models import Batch,Student,Course,Teacher,Subject
from .serializers import Courseserializer1,Subjectserializer,Subjectserializer1,Batchserializer,Batchserializer1,Courseserializer,Courseserializer2,Subjectserializer2,Batchserializer2
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.
class CourseInfo(APIView):
    def get(self,request):
        course_list=Course.objects.all()
        serializer=Courseserializer(course_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        course1=request.data.get('course1')
        serializer=Courseserializer2(data=course1)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)    
    
class Courseid(APIView):
    def get(sef,request,id):
        course2=Course.objects.get(id=id)
        serializer=Courseserializer(course2)
        return Response(serializer.data) 
    
    def delete(self,request,id):
        course3=Course.objects.get(id=id)
        course3.delete()
        return Response({"messge":"course deleted"})
      
    def put(self,request,id,format=None):
        course4=Course.objects.get(id=id)
        serializers=Courseserializer1(course4,data=request.data)
        if serializers.is_valid():
            serializers.save()  
            return Response(serializers.data)
        
class Coursename(APIView):
    def get(self,request,name):
        course5=Course.objects.get(name=name)
        serializer=Courseserializer(course5)
        return Response(serializer.data)
    
    
class SubjectInfo(APIView):
    def get(self,request):
        subject1=Subject.objects.all()
        serializer=Subjectserializer1(subject1,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        subject2=request.data.get('subject2')
        serializer=Subjectserializer1(data=subject2)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"subject added"})
        
class Subjectid(APIView):
    def get(sef,request,id):
        subject3=Subject.objects.get(id=id)
        serializer=Subjectserializer1(subject3)
        return Response(serializer.data) 
    
    def delete(self,request,id):
        subject4=Subject.objects.get(id=id)
        subject4.delete()
        return Response({"messge":"subject deleted"})
            
    def put(self,request,id):
        subject5=Subject.objects.get(id=id)
        serializers=Subjectserializer1(subject5,data=request.data)
        if serializers.is_valid():
            serializers.save()  
            return Response(serializers.data)

        
class BatchInfo(APIView):
    def get(self,request):
        batch_1=Batch.objects.all()
        serializer=Batchserializer(batch_1,many=True)
        return Response(serializer.data)    
    
    def post(self,request):
        batch_2=request.data.get('batch_2')
        serializer=Batchserializer1(data=batch_2)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"batch added"})
    
class Batchid(APIView):
    def get(self,request,id):
        batch_3=Batch.objects.get(id=id)
        serializer=Batchserializer1(batch_3)
        return Response(serializer.data) 
            
    def delete(self,request,id):
        batch_4=Batch.objects.get(id=id)
        batch_4.delete()
        return Response({"messge":"batch deleted"})
    
    def put(self,request,id,format=None):
        batch_5=Batch.objects.get(id=id)
        serializers=Batchserializer1(batch_5,data=request.data)
        if serializers.is_valid():
            serializers.save()  
            return Response(serializers.data)
        
