from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Venues



def test(request):
	test_param = int(request.GET.get('test_param', 99999))
	print(test_param)
	return HttpResponse("Hello World." + str(test_param))

def home(request):
	return render(request, 'venues/home.html')

def view_venues(request):
	data = Venues.objects.all()
	print(data)
	return render(request, 'venues/list.html', {'data' : data})

def venue_more_info(request):
	#data = Venues.objects.all()
	#print(data)
	venue = request.GET.get('venue', "none selected")
	venue_object = Venues.objects.get(name=venue)
	print(venue_object.name)
	print(venue_object.url)
	return render(request, 'venues/venue_info.html', {'venue' : venue_object})