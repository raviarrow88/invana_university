from django.shortcuts import render

# Create your views here.
from .models import Course,Video

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
import urllib


def course_list(request):
    queryset_list = Course.objects.all()
    context ={'object_list':queryset_list}

    return render(request,"course-list.html",context)



def course_detail(request, id):
    course = get_object_or_404(Course,id=id)
    videos = course.videos.all()
    context = {'course':course,
        'videos':videos}
    return render(request,"course-detail.html",context)