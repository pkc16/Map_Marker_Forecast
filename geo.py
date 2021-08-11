from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker
import configparser
import os

# inherit from Marker class in folium
class Geopoint(Marker):

	def __init__(self, latitude, longitude):
		super().__init__(location = [latitude, longitude])
		self.latitude = latitude
		self.longitude = longitude

	def closest_parallel(self):
		return round(self.latitude)

	def get_antipode(self):
		# get the coordinates of the location on the opposite side of the Earth
		antipode_latitude = self.latitude * -1

		# Add 180 for negative longitudes; subtract 180 for positive longitudes
		if self.longitude <= 0:
			antipode_longitude = self.longitude + 180
		else:
			antipode_longitude = self.longitude - 180

		return [antipode_latitude, antipode_longitude]

	def get_time(self):
		# get the time
		timezone_str = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
		time_now = datetime.now(timezone(timezone_str))
		return time_now

	def get_weather(self):
		# get parameters from config file
		# first get the current directory
		cur_dir = os.path.dirname(__file__)

		# generate the absolute filepath of the output file
		config_filename = "MapMarkerForecast_config.txt"
		config_filepath = os.path.join(cur_dir, config_filename)

		# now get the info from the config file and set variables
		parser = configparser.ConfigParser()
		parser.read_file(open(config_filepath))
		api_key = parser.get('Settings', 'api_key')

		weather = Weather(apikey = api_key, lat = self.latitude, lon = self.longitude)
		#return weather.next_12h_simplified()
		forecast = weather.next_12h_simplified()

		# for item in forecast:
		# 	time = item[0][0][-8:-6]
		# 	print(time)
		# 	if int(time) > 12:
		# 		print(f"time {time} is greater than 12")

		# 	else:
		# 		print(f"time {time} is less than 12")

		return weather.next_12h_simplified()


	@classmethod	#allows the function to be called without having to instantiate the class the function is in
	def random(cls):
		return cls(latitude = uniform(-90, 90), longitude = uniform(-180, 180))