from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
