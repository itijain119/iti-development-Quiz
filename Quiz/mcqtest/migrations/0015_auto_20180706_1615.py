# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-06 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mcqtest', '0014_auto_20180706_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiveQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_sno', models.CharField(max_length=10)),
                ('ques_text', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correct', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_enrollmentno', models.IntegerField()),
                ('student_phoneno', models.IntegerField()),
                ('student_father_name', models.CharField(max_length=100)),
                ('student_mother_name', models.CharField(max_length=100)),
                ('student_address', models.CharField(max_length=200)),
                ('student_pic', models.ImageField(default='noimage.jpg', upload_to='pic_folder/')),
                ('student_city', models.CharField(max_length=30)),
                ('student_state', models.CharField(max_length=30)),
                ('student_pincode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=40)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentanswers', to='mcqtest.Question')),
            ],
        ),
        migrations.CreateModel(
            name='TakenQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField()),
                ('quizgiven', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='takenquizs', to='mcqtest.Quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='takenquizs', to='mcqtest.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_sno', models.IntegerField()),
                ('teacher_salary', models.IntegerField()),
                ('teacher_qualification', models.CharField(max_length=100)),
                ('teacher_phoneno', models.IntegerField()),
                ('teacher_address', models.CharField(max_length=200)),
                ('teacher_pic', models.ImageField(default='noimage.jpg', upload_to='pic_folder/')),
                ('teacher_city', models.CharField(max_length=30)),
                ('teacher_state', models.CharField(max_length=30)),
                ('teacher_pincode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='mcqtest.Teacher'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='mcqtest.Quiz'),
        ),
        migrations.AddField(
            model_name='givequiz',
            name='quizname',
            field=models.ManyToManyField(related_name='givequizs', to='mcqtest.Quiz'),
        ),
        migrations.AddField(
            model_name='givequiz',
            name='student',
            field=models.ManyToManyField(related_name='givequizs', to='mcqtest.Student'),
        ),
    ]