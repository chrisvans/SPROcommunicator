from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.timezone import utc, get_current_timezone
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
#from LMcommunicator.models import ....
import datetime


def home(request):
	return render(request, 'home.html')

def graph(request):
	shotdata = []
	pressuredata = []
	for number in range(30):
		shotdata.append(int(number))
	html_params = {
	               'shotdata':shotdata
	              }
	return render(request, 'graph.html', html_params)

def graph_chart(request):
	return render(request, 'graph_chart.html')