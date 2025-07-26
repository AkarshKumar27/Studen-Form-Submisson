# student_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Yeh line 'students' app ke URLs ko project se jodti hai.
    # Make sure this line is present.
    path('', include('students.urls')),
]
