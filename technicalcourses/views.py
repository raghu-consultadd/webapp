from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Allcourses,details
from django.template import loader
def Courses(request):
    ac = Allcourses.objects.all()
    template=loader.get_template('technicalcourses/courses.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))
def detail(request, course_id):
    course=get_object_or_404(Allcourses,pk=course_id)
    return render(request,'technicalcourses/detail.html',{'course':course})

    #return render(request,'technicalcourses/detail.html',{'course':course})
def yourchoice(request,course_id):
    course=get_object_or_404(Allcourses,pk=course_id)
    try:
        selected_ct=course.details_set.get(pk=request.POST['choice'])
    except (KeyError, Allcourses.DoesNotExist):
        return render(request,'Allcourses/detail.html',{
            'course':course,
        'error_message':"select a valid option"
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request,'technicalCourses/detail.html',{'course':course})







# Create your views here.
