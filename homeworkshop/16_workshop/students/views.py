from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    student = Student.objects.all()
    context = {
        'students': student,
    }
    return render(request, 'students/index.html', context)

# 1. create
def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    student = Student(name=name, email=email, birthday=birthday, age=age,)
    student.save()
    return redirect('/students/')

# 2. read
def detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student,}
    return render(request, 'students/detail.html', context)

# 3. DELETE
def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')

# 4. UPDATE
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student,}
    return render(request, 'students/edit.html', context)

def update(request, pk):
    student = Student.objects.get(pk=pk)

    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    
    return redirect(f'/students/{student.pk}')