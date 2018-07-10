from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from mcqtest import models
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.views.generic import TemplateView
from random import randint


@login_required
def createquiz(request):
        return render(request,"mcqtest/teacher/createquiz.html")

@login_required
def submitquiz(request):
    if request.method=='POST':
        obj = models.Teacher.objects.get(user=request.user)
        quizname = request.POST.get('quizname')
        existquiz = models.Quiz.objects.all()
        for i in existquiz:
            if i.quiz_name == quizname:
                return render(request, "mcqtest/teacher/createquiz.html",{'message':'Quiz already exist.Create Another Quiz'})
        objquiz = models.Quiz()
        objquiz.owner = obj
        objquiz.quiz_name = quizname
        objquiz.save()
        request.session["quiz_name"] = quizname
        return HttpResponseRedirect('/main/quizform')
    else:
        return HttpResponse("Create Quiz First")

@login_required
def quizform(request):
    if request.session['user_type'] == 'teacher':
        return render(request,"mcqtest/teacher/quizform.html")
    else:
        return HttpResponseRedirect('/main/createquiz')

@login_required
def submitform(request):
    if request.method == 'POST':
        qno = request.POST.get('qno')
        quescont = request.POST.get('quescontent')
        opt1 = request.POST.get('opt1')
        opt2 = request.POST.get('opt2')
        opt3 = request.POST.get('opt3')
        opt4 = request.POST.get('opt4')
        correct = request.POST.get('correct')
        quizname = request.session["quiz_name"]
        objquiz = models.Quiz.objects.get(quiz_name = quizname)
        objques = models.Question()
        objques.quiz = objquiz
        objques.ques_sno = qno
        objques.ques_text = quescont
        objques.option1 = opt1
        objques.option2 = opt2
        objques.option3 = opt3
        objques.option4 = opt4
        objques.correct = correct
        objques.save()
        return HttpResponseRedirect('/main/quizform')

    else:
        return HttpResponse("Form Not Filled")

@login_required
def showques(request):
    quizname = request.session["quiz_name"]
    quiz = models.Quiz.objects.get(quiz_name = quizname)
    allques = quiz.questions.all()
    return render(request,"mcqtest/teacher/showques.html" , {'allques' : allques})

@login_required
def allquiz(request):
    user = models.Teacher.objects.get(user = request.user)
    allquiz = user.quizs.all()
    return render(request,'mcqtest/teacher/allquiz.html',{'allquiz' : allquiz})

@login_required
def showresult(request , pk):
    quiz = models.Quiz.objects.get(pk = pk)
    studenttakequiz = quiz.takenquizs.all()
    average = quiz.takenquizs.all().aggregate(averagescore = Avg('marks'))
    return render(request,'mcqtest/teacher/showresult.html',{'student':studenttakequiz ,'average' : average})
