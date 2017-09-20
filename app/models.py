from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 100)
    title_extended = models.CharField(max_length = 255)
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    gender = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=20)
    father = models.ForeignKey('Father')
    mother = models.ForeignKey('Mother')
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    related = models.CharField(max_length=100)
    entry_year = models.DateField()
    graduation_year = models.DateField()
    level = models.CharField(max_length=10) # BA, MSc Phd
    student_type = models.CharField(max_length=1)
    passport_id = models.IntegerField()
    number = models.IntegerField()
    unt = models.IntegerField()
    attestat_number = models.IntegerField()
    attestat_date = models.DateField()
    attestat_type = models.CharField(max_length=12)
    payment = models.CharField(max_length=9)
    certificate_number = models.IntegerField()

class Father(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

class Mother(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job = models.CharField(max_length=60)
    phone = models.CharField(max_length=12)
    email = models.EmailField()