from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.timezone import utc, get_current_timezone
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from LMcommunicator.models import StatusSnapshot
import datetime
import random
import time

# Javascript's strftime
# (JavaScript Object Notation)

class ViewManager():
	def get_dataset(self, identity):
		queryset = StatusSnapshot.objects.filter(identity=identity)
		status_list = []
		timestamp_list = []
		for status_object in queryset:
			format_test = float(status_object.status)
			status_list.append(format_test)
			format_test2 = status_object.get_timestamp()
			timestamp_list.append(format_test2)
			print status_object, format_test, format_test2
		return [status_list, timestamp_list]


def home(request):
    view_manager = ViewManager()

    main_boiler_1_data = view_manager.get_dataset('main_boiler_1_actual_temp')
    main_boiler_2_data = view_manager.get_dataset('main_boiler_2_actual_temp')
    passed_params = {
    'main_boiler_1_temperature':main_boiler_1_data[0],
    'main_boiler_1_timestamp':main_boiler_1_data[1],
    'main_boiler_2_temperature':main_boiler_2_data[0],
    'main_boiler_2_timestamp':main_boiler_2_data[1],
    }
    return render(request, 'home.html', passed_params)

def generate_objects(request):
	# Test data to populate charts.
	counter1 = time.time()
	temperature = ''
	obj1 = StatusSnapshot()
	obj1.set_status('main_boiler_2_set_temp', '197.5')
	current_time = timezone.now()
	obj1.timestamp = current_time
	obj2 = StatusSnapshot()
	obj2.set_status('steam_boiler_set_temp', '210.0')   
	obj2.timestamp = current_time
	obj1.save()
	obj2.save()
	while True:
		counter = time.time()
		if ((counter1 - counter) % 2) == 0:
			temperature = '197.' + str(random.randrange(0, 9, 1))
			obj_a = StatusSnapshot()
			obj_a.set_status('main_boiler_2_actual_temp', temperature)
			current_time = timezone.now()
			obj_a.timestamp = current_time
			steam_temp = '21' + str(random.randrange(4, 9, 1)) + '.' + str(random.randrange(0, 9, 1))
			obj_b = StatusSnapshot()
			obj_b.set_status('steam_boiler_actual_temp', steam_temp)
			obj_b.timestamp = current_time
			obj_a.save()
			obj_b.save()
		if counter - counter1 > 30:
			break
		print counter, counter1

	return render(request, 'home.html')

# main_boiler_1_set_temp
# main_boiler_2_set_temp
# main_boiler_1_actual_temp
# main_boiler_2_actual_temp
# steam_boiler_set_temp
# steam_boiler_actual_temp
# level_sensor_1
# level_sensor_2
# pump_status
# group_1_status
# group_1_flow
# group_2_status
# group_2_flow
# group_3_status
# group_3_flow
# group_4_status
# group_4_flow
# steam_boiler_fill
# tea_tap_status
# left_auto_steam_status
# right_auto_steam_status
# cup_warmer_status
# var format = d3.time.format("%Y-%m-%d");
# format.parse("2011-01-01"); // returns a Date
# so you tell the format what part is what
# then give it a string (or the 0th element of your x,y array) and it will know that 2011 is the year, 01 is the month, and 01 is the day
# datetime should look something like 2007-12-31 23:59:59.999999

# which would be %Y-%m-%d %H:%m%s