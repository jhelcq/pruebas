from django.shortcuts import render
import config
import ee

# Create your views here.

def inicio(request):
	return render_to_response('index.html')