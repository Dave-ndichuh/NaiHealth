from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    yob = models.DateField()

    def __str__(self):
        return self.fullname


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.EmailField()
    phonenumber= models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__ (self):
        return self.firstname + self.lastname

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model): #for the login form
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
