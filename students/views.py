# students/views.py

from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Form save karne par student object milta hai
            student = form.save() 
            # Redirect to the success page with the new student's ID
            return redirect('success_page', student_id=student.id)
    else:
        form = StudentForm()
    
    return render(request, 'students/student_form.html', {'form': form})


def success_view(request, student_id):
    try:
        # ID se student ka data database se nikalein
        student = Student.objects.get(id=student_id)
        # Data ko template mein render karein
        return render(request, 'students/success.html', {'student': student})
    except Student.DoesNotExist:
        # Agar galat ID hai to form par wapas bhej dein
        return redirect('student_form')
