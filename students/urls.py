# students/urls.py

from django.urls import path
from .views import student_form_view, success_view

# The error you are seeing is because Django cannot find this 'urlpatterns' list
# in your students/urls.py file.
# Please ensure your file has this exact content.
urlpatterns = [
    path('', student_form_view, name='student_form'),
    path('success/<int:student_id>/', success_view, name='success_page'),
]
