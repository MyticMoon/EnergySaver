
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.db import connection, transaction
# import models
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response, redirect
from random import randint
#
def index(request):
    # t = get_template('iwantit/index.html')
    # mainBody = t.render(Context({}))
    #return HttpResponse('This is first page of energy saver')
    return render_to_response('index.html', None)

def approach(request):
    # t = get_template('iwantit/index.html')
    # mainBody = t.render(Context({}))
    #return HttpResponse('This is first page of energy saver')
    return render_to_response('approach.html', None)


def socialView(request):
    return render_to_response('social.html', None)


def personalView(request):
    return render_to_response('personal.html', None)