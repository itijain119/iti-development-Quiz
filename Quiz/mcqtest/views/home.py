from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from mcqtest import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def home(request):
    return render(request,'mcqtest/home/home.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password is successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

@login_required
def profile(request):
    try:
        student = models.Student.objects.get(user =  request.user)
    except:
        student = None
    try:
        teacher = models.Teacher.objects.get(user = request.user)
    except:
        teacher = None

    user = request.user

    if student:
        request.session['user_type'] = 'student'
        return render(request,"mcqtest/student/student.html",{'student':student,'user' :user})
    elif teacher:
        request.session['user_type'] = 'teacher'
        return render(request,"mcqtest/teacher/teacher.html",{'teacher':teacher,'user':user})
    else:
        return render(request,"mcqtest/home/home.html")
