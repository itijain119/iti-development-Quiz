from django.conf.urls import url
from .views import home,student,teacher

urlpatterns =[
    url(r'profile/', home.profile , name = 'profile'),
    url(r'createquiz/', teacher.createquiz),
    url(r'submitquiz/', teacher.submitquiz),
    url(r'quizform/', teacher.quizform),
    url(r'^submitform/', teacher.submitform),
    url(r'^showques/', teacher.showques , name = 'showques'),
    url(r'^allquiz/', teacher.allquiz),
    url(r'^showresult/(?P<pk>\d+)/', teacher.showresult , name = 'showresult'),


    url(r'^availablequiz/', student.availablequiz),
    url(r'^givenquizzes/', student.givenquizzes),
    url(r'^instruction/(?P<pk>\d+)/', student.instruction , name='instruction'),
    url(r'^givequiz/', student.givequiz , name = 'givequiz'),
]