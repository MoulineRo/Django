from django.db import models
from faker import Faker

fake = Faker()
fname = fake.name()
fage = fake.random_int(min=30, max=50)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)


bar = Student.objects.create(name=fname, age=fage)


class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

for _ in range(10):
    s = Students.objects.create(name=fake.name(), age=fake.random_int(min=30, max=50))
