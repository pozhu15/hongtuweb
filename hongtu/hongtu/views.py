from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
import datetime

# Create your views here.

def index(request):
	
	template = loader.get_template('index.html')
	context = {
	'latest': 2212,
	'now': datetime.datetime.now(),
	}
	return HttpResponse(template.render(context, request))

def detail(request):

    context = {'latest_question_list': 0}
    return render(request, 'detail.html', context)



