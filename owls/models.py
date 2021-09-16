from django.db import models
from django.contrib import admin

class Page(models.Model):
    student_name = models.CharField(max_length=128)
    student_number = models.CharField(max_length=128)
    student_address = models.CharField(max_length=512)

    def __unicode__(self):
        return self.student_name

class PageAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_number', 'student_address')

    def __unicode__(self):
        return self.list_display
