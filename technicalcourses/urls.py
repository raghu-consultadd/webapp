from django.urls import path
from . import views


app_name='technicalcourses'

urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
    path('', views.Courses,name='Home-Page'),
]
