# students/admin.py

from django.contrib import admin
from .models import Student

# Student model ko admin site par register karein
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Admin panel mein kaun kaun si fields dikhni chahiye
    list_display = ('unique_id', 'student_name', 'course', 'email', 'submission_date')
    
    # Kin fields ke basis par search kar sakein
    search_fields = ('student_name', 'email', 'unique_id', 'course')
    
    # Kin fields ke basis par filter kar sakein
    list_filter = ('course', 'submission_date')
    
    # Fields ko read-only banayein (taaki galti se edit na ho)
    readonly_fields = ('unique_id', 'submission_date')

