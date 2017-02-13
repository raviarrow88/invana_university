from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField()
    youtube_id = models.CharField(max_length=100,null=True,blank=True)
    playlist_id =models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField(upload_to=None,null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")

    def __str__(self):
        return self.title


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=300,null=True,blank=True)
    created_by =models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=None,null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")

    videos = models.ManyToManyField(Video)

    def __str__(self):
        return self.course_title



