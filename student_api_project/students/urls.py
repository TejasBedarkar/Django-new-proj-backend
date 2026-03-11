from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:id>/', views.update_student),
    path('students/delete/<int:id>/', views.delete_student),
    path('register/', views.register),
    path('login/', views.login_user),
]