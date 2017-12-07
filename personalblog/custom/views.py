from django.shortcuts import render
from django.http import HttpResponse
import json
from bson import json_util
import os.path
import math

def home_page(request):
	return render(request, 'custom/home.html', {})
