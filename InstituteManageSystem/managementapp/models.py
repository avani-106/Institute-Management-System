from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    fees=models.IntegerField()
    duration=models.IntegerField()
   
class Batch(models.Model):
    start_date=models.DateField()  #(yy-mm-date)
    start_time=models.TimeField()  #(hr,min,sec)
    end_time=models.TimeField()
    courses= models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    batch1=models.ManyToManyField(Batch,related_name="batches1") 
    
    
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    experience=models.IntegerField()
    batch2=models.ManyToManyField(Batch,related_name="batches2")    

class Subject(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    course=models.ManyToManyField(Course,related_name="subjects")
    teacher=models.ManyToManyField(Teacher,related_name="teachers")

   