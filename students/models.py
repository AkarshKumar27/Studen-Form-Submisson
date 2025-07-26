# students/models.py

from django.db import models
import uuid
from django.utils import timezone # Ise import karein

class Student(models.Model):
    # Course ke options
    COURSE_CHOICES = [
        ('B.Tech CSE', 'B.Tech - Computer Science'),
        ('B.Tech IT', 'B.Tech - Information Technology'),
        ('B.Tech ECE', 'B.Tech - Electronics & Communication'),
        ('B.Tech ME', 'B.Tech - Mechanical Engineering'),
        ('BCA', 'BCA - Bachelor of Computer Applications'),
        ('M.Tech CSE', 'M.Tech - Computer Science'),
        ('M.Tech IT', 'M.Tech - Information Technology'),
    ]

    # Fields
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    qualification_percentage = models.FloatField()
    unique_id = models.CharField(max_length=50, unique=True, blank=True)
    # Yeh field waise hi rahegi
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

    def save(self, *args, **kwargs):
        # Jab naya student save ho, tab ek unique ID banayein
        if not self.unique_id:
            # FIX: self.submission_date ke bajaye timezone.now() ka istemal karein
            # kyunki save ke dauran submission_date abhi set nahi hui hai.
            now = timezone.now()
            self.unique_id = f"STU-{now.year}-{str(uuid.uuid4())[:8].upper()}"
        super().save(*args, **kwargs)
