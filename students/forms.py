# students/forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_name', 
            'date_of_birth', 
            'course', 
            'email', 
            'mobile_number', 
            'qualification_percentage'
        ]
        # Form fields ko sundar labels dene ke liye
        labels = {
            'student_name': 'Full Name',
            'date_of_birth': 'Date of Birth',
            'course': 'Select Course',
            'email': 'Email Address',
            'mobile_number': 'Mobile Number',
            'qualification_percentage': '12th/Diploma Percentage',
        }
        # Date field ke liye HTML5 date picker widget
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    # Custom validation for qualification percentage
    def clean_qualification_percentage(self):
        percentage = self.cleaned_data.get('qualification_percentage')
        if percentage < 75:
            raise forms.ValidationError("Sorry, the minimum qualification criteria is 75%.")
        return percentage
