from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import utc, get_current_timezone
import datetime

class StatusSnapshot(models.Model):
	identity = models.CharField(max_length=55)
	status = models.CharField(max_length=55)
	timestamp = models.DateTimeField(null=True)

	def set_status(self, identity=None, status=None):
		self.identity = identity
		self.status = status

	def get_timestamp(self):
		true_timestamp = self.timestamp.replace(tzinfo=get_current_timezone())
		true_timestamp = true_timestamp.strftime('%I%M%S')
		true_timestamp = int(true_timestamp)
		return true_timestamp

#self.timestamp.replace(tzinfo=get_current_timezone())

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