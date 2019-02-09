from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings



def test(request):
	return HttpResponse("Hello World.")

def home(request):
	return render(request, 'venues/list.html')

