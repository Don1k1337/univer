from django.db import models
from students.models import  Major

class Course(models.Model):
    title = models.CharField(max_length=40, default='')
    description = models.CharField(max_length=60)
    language = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=40, default='')
    ccode = models.CharField(max_length=4)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return self.abbreviation

