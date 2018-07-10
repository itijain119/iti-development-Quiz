from django.contrib import admin
from mcqtest import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.GiveQuiz)
admin.site.register(models.TakenQuiz)
admin.site.register(models.StudentAnswer)