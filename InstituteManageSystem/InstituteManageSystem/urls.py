"""InstituteManageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from managementapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course',views.CourseInfo.as_view()),
    path('course/<int:id>',views.Courseid.as_view()),
    path('course/<str:name>',views.Coursename.as_view()),
    path('subject',views.SubjectInfo.as_view()),
    path('subject/<int:id>',views.Subjectid.as_view()),
    path('batch',views.BatchInfo.as_view()),
    path('batch/<int:id>',views.Batchid.as_view())
    
]
