from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Student, Students

fake = Faker()
fname = fake.name()
fage = fake.random_int(min=30, max=50)


def student(request):
    latest1 = Student.objects.latest('id').name
    latest2 = Student.objects.latest('id').age
    res = latest1 + ' ' + str(latest2)
    return HttpResponse(res)


def index(request):
    return render(request, "index.html")


def postuser(request):
    age = int(request.POST.get("age", 1))
    res = []
    if age > 0 and age <= 100:
        for _ in range(age):
            s = Students.objects.create(name=fake.name(), age=fake.random_int(min=30, max=50))
            res.append(s.name + ' ')
            res.append(str(s.age) + ' ')
        return HttpResponse(res)
    if age == 0:
        return HttpResponse('Вы ввели нуль')
    else:
        return render(request, "error.html")
