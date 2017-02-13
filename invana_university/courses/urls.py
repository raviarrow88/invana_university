from . import views
from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^courses/$', views.course_list, name="course_list"),
    url(r'^course/(?P<id>\d+)/$', views.course_detail,name= 'course_detail'),




]