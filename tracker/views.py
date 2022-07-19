from django.template import RequestContext
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseNotAllowed
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.template.loader import render_to_string
from wsgiref.util import FileWrapper
from django.conf import settings
from http.client import HTTPConnection
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from os.path import dirname, join
from tracker.models import instructor
from tracker.forms import instructorNameForm
import uuid
import mimetypes
import os
import shutil
import re
import time


def index (request):
        print("in index")
        # person = instructor()
        # person.name = "dude"
        # person.instructorID = str(uuid.uuid4())
        # person.save()
        print("saved")
        return render(request, "index.html", { },)
        return HttpResponse("howdy asshole welcome to jackass")

def addInstructor (request):
    if request.method =='POST':
        print("BLAH")
    else:
        form = instructorNameForm()
        return render(request, "addInstructor.html", {'form': form,}, )
    return render(request, "addInstructor.html", { },)

def instructorListView(request):
    return HttpResponse("howdy asshole welcome to jackass")
    print("view")

    instructors = instructor.objects.all()
    return render(request, "instructors.html", {'instructors': instructors,},)
    return HttpResponse("howdy asshole welcome to jackass")

def addStudent(request):
    return render(request, "index.html", { },)
    return HttpResponse("howdy asshole welcome to jackass")
def studentList(request):
    return render(request, "index.html", { },)
    return HttpResponse("howdy asshole welcome to jackass")
# Create your views here.
