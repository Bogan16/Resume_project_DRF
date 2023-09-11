from django.db import models

class Resume(models.Model):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    year_of_birth = models.DateField()
    skills = models.TextField()
    educations = models.TextField()

    def __str__(self):
      return f"{self.name} {self.surname}"