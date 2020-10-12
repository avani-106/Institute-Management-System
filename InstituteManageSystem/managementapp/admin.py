from django.contrib import admin
from .models import Batch,Student,Course,Teacher,Subject
# Register your models here.
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Subject)