from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect, HttpResponse
from mcqtest import models
from django.contrib.auth.decorators import login_required


@login_required
def availablequiz(request):
    quizzes = []
    allquiz = models.Quiz.objects.all()
    studentname = models.Student.objects.get(user = request.user)
    takenquiz = models.TakenQuiz.objects.filter(student = studentname)
    for a in allquiz:
        flag = 0
        for b in takenquiz:
            if str(a.quiz_name) == str(b.quizgiven):
                flag = 1
                break
        if flag == 0:
            quizzes.append(a)

    return render(request,'mcqtest/student/availablequiz.html',{'quizs' : quizzes})


@login_required
def givenquizzes(request):
    studentname = models.Student.objects.get(user=request.user)
    givenquizzes = models.TakenQuiz.objects.filter(student=studentname)
    return render(request , 'mcqtest/student/givenquizzes.html' ,{'allquizzes' : givenquizzes})


@login_required
def instruction(request,pk):
    quiz = models.Quiz.objects.get(pk=pk)
    quizname = quiz.quiz_name
    request.session["quiz"] = quizname
    request.session['count'] = 0
    request.session['answer'] = 0
    return render(request , 'mcqtest/student/instruction.html')


@login_required
def givequiz(request):
    quizname = request.session['quiz']
    quiz = models.Quiz.objects.get(quiz_name = quizname)
    Qset = quiz.questions.all().order_by('id')
    d = Qset[int(request.session['count'])]
    if request.method == 'POST':
        ans = request.POST.get('youranswer')
        if str(d.correct) == str(ans):
            request.session['answer'] = str(int(request.session['answer'])+1)
        request.session['count'] = str(int(request.session['count']) + 1)
        if int(request.session['count']) >= len(Qset):
            marks = request.session['answer']
            objquiz = models.TakenQuiz()
            objquiz.student = models.Student.objects.get(user = request.user)
            objquiz.quizgiven = quiz
            objquiz.marks = marks
            objquiz.save()
            return render(request,'mcqtest/student/quizcomplete.html',{'marks':marks})
        else:
            d = Qset[int(request.session['count'])]
            return render(request, "mcqtest/student/givequiz.html", {"quest": d})
    else:
        return render(request, "mcqtest/student/givequiz.html", {"quest": d,})

