from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teacher_login(request):
    return render(request, 'teacher_login.html')

def student_login(request):
    return render(request, 'student_login.html')

