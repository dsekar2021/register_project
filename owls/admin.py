from django.contrib import admin
from owls.models import Page, PageAdmin

admin.site.register(Page, PageAdmin)
