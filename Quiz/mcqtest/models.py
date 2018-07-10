from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student_enrollmentno = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_phoneno = models.IntegerField()
    student_father_name = models.CharField(max_length=100)
    student_mother_name = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)
    student_pic = models.ImageField(upload_to='pic_folder/',default='noimage.jpg')
    student_city = models.CharField(max_length=30)
    student_state = models.CharField(max_length=30)
    student_pincode = models.IntegerField()

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    teacher_sno = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    teacher_salary = models.IntegerField()
    teacher_qualification = models.CharField(max_length = 100)
    teacher_phoneno = models.IntegerField()
    teacher_address = models.CharField(max_length=200)
    teacher_pic = models.ImageField(upload_to='pic_folder/' , default='noimage.jpg')
    teacher_city = models.CharField(max_length=30)
    teacher_state = models.CharField(max_length=30)
    teacher_pincode = models.IntegerField()

    def __str__(self):
        return self.user.username


class Quiz(models.Model):
    owner = models.ForeignKey(Teacher , on_delete=models.CASCADE ,related_name = 'quizs')
    quiz_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE , related_name = 'questions')
    ques_sno = models.CharField(max_length=10)
    ques_text = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct = models.CharField(max_length=100)

    def __str__(self):
        return self.ques_sno


class GiveQuiz(models.Model):
    student = models.ManyToManyField(Student , related_name = 'givequizs')
    quizname = models.ManyToManyField(Quiz , related_name = 'givequizs')

    def __str__(self):
        return self.student.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE , related_name = 'takenquizs')
    quizgiven  = models.ForeignKey(Quiz , on_delete=models.CASCADE , related_name = 'takenquizs')
    marks  = models.FloatField()

    def __str__(self):
        return self.student.user.username

class StudentAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE , related_name = 'studentanswers')
    answer = models.CharField(max_length = 40)

    def __str__(self):
        return self.quiz.quiz_name
