from rest_framework import serializers
from .models import Batch,Student,Course,Teacher,Subject

class Subjectserializer2(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=('id',)
        
class Courseserializer2(serializers.ModelSerializer):
    subjects=Subjectserializer2(many=True,read_only=True)
    class Meta:
        model=Course
        fields=('name','fees','duration','subjects')        
        
class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields="__all__"        
            
class Courseserializer1(serializers.ModelSerializer):
    subjects_id=Subjectserializer(many=True,source="course.id",read_only=True)
    class Meta:
        model=Course
        fields=('name','fees','duration','subjects_id')
    
class Subjectserializer1(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=('id','name','description')

class Courseserializer(serializers.ModelSerializer):
    subjects=Subjectserializer1(many=True,read_only=True)
    class Meta:
        model=Course
        fields=('name','fees','duration','subjects')
    
class Batchserializer(serializers.ModelSerializer):
    courses=Courseserializer(read_only=True)
    class Meta:
        model=Batch
        fields=('start_date','start_time','end_time','courses')       

class Batchserializer1(serializers.ModelSerializer):
    course_id=serializers.IntegerField(source="courses.id",read_only=True)
     
    class Meta:
        model=Batch
        fields=('start_date','start_time','end_time','course_id')



class Batchserializer2(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields=('start_date','start_time','end_time') 
            