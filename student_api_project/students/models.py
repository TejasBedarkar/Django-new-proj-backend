from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):               #This controls how the object appears in Django Admin Panel
        return self.name
