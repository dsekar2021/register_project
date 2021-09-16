# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from owls.models import Page

def index(request):
    context = RequestContext(request)
    student_list = Page.objects.all()
    context_dict = {'students': student_list}
    return render_to_response('owls/index.html', context_dict, context)
