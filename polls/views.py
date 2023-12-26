from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    context = {"page": "Index"}
    return render(request, 'index.html', context)


def home(request):

    users = User.objects.all()

    context = {"page": "All Users",'users':users}

    return render(request, 'home.html', context)


# register a user
def register(request):
    if request.method == "POST":
        data = request.POST

        # check if username already exits
        user = User.objects.filter(username=data.get('username'))
        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            username=data.get('username')
        )
        user.set_password(data.get('password'))
        user.save()
        messages.info(request, "New user registered successfully...")
        return redirect('/register/')

    context = {"page": "Register New User"}
    return render(request, 'register.html', context)


# login a user
def login(request):
    context = {"page": "User Login Page"}

    if request.method =='POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username = username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/userList/')


    return render(request, 'login.html', context)


# add new student to database
def createStudent(request):
    if request.method == "POST":
        data = request.POST
        Student.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            dob=data.get("dob"),
            roll_no=data.get("roll_no"),
            program=data.get("program"),
            is_adult=data.get("is_adult"),
            image=request.FILES.get("image"),
            user_id=request.user.id
        )
        messages.info(request, "Student registered successfully...")
        return redirect('/students')

    return render(request, 'addStudent.html')


# pass list of students to view
def students(request):
    students = Student.objects.all()
    context1 = {}
    # for search
    if request.GET.get('search'):
        search = request.GET.get('search')
        students = students.filter(name__icontains=search)
        context1 = {'search': search}

    context2 = {"students": students, "page": "Students Info"}
    context = {**context2, **context1}
    return render(request, 'students.html', context)


# update a record
def updateStudent(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        student.name = data.get('name')
        student.roll_no = data.get('roll_no')
        student.email = data.get('email')
        student.program = data.get('program')
        student.is_adult = data.get('is_adult')
        student.dob = data.get('dob')
        student.user_id = request.user.id
        if request.FILES.get("image"):
            student.image = request.FILES.get('image')

        student.save()
        messages.info(request, "Student Record Updated successfully...")
        return redirect('/students')

    student.dob = student.dob.strftime('%Y-%m-%d')
    HttpResponse(student.dob)
    context = {"student": student, "page": "Update Student Info"}
    return render(request, 'update_student.html', context)


# delete a record
def delStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.info(request, "Student Record Deleted successfully...")
    return redirect('/students')
