# This program sets marker(s) on a map with a popup that has the weather forecast

from folium import Map, Marker, Popup
from geo import Geopoint
from geopy.geocoders import Nominatim
import webbrowser
import configparser
import os

# get parameters from config file
# first get the current directory
cur_dir = os.path.dirname(__file__)

# generate the absolute filepath of the output file
config_filename = "MapMarkerForecast_config.txt"
config_filepath = os.path.join(cur_dir, config_filename)

# now get the info from the config file and set variables
parser = configparser.ConfigParser()
parser.read_file(open(config_filepath))
file_loc = parser.get('Settings', 'output_file')
api_key = parser.get('Settings', 'api_key')

# Prompt for the location
input_location = ""
while not input_location:
	input_location = input("Enter City or City, State or ZIP: ")

input_nation = input("Enter Country (default is US): ")
if not input_nation or input_nation.upper() == "US" or input_nation.upper() == "USA":
	# default to US
	input_nation = "US"


geolocator = Nominatim(user_agent="my_user_agent")
country = input_nation
loc = geolocator.geocode(input_location +','+ country)

latitude = loc.latitude
longitude = loc.longitude
location = [latitude, longitude]

# Create map
mymap = Map(location = location)

point = Geopoint(latitude=latitude, longitude=longitude, api_key=api_key)
forecast = point.get_weather()
#print(forecast)

# set the weather popup
popup_content = ""
for index,item in enumerate(forecast,0):
	popup_content = popup_content + f"""{forecast[index][0][-8:-6]}h: {round(forecast[index][1])}°F 
	<img src="http://openweathermap.org/img/wn/{forecast[index][-1]}@2x.png" width=35><hr style="margin:1px">"""
		
# make the times in the popup user-friendly
popup_content = popup_content.replace("00h", "12 am")
popup_content = popup_content.replace("03h", "3 am")
popup_content = popup_content.replace("06h", "6 am")
popup_content = popup_content.replace("09h", "9 am")
popup_content = popup_content.replace("12h", "12 pm")
popup_content = popup_content.replace("15h", "3 pm")
popup_content = popup_content.replace("18h", "6 pm")
popup_content = popup_content.replace("21h", "9 pm")

popup = Popup(popup_content, max_width=400)
popup.add_to(point)

point.add_to(mymap)

# for lat, lon in locations:
# 	# Create Geopoint instance
# 	point = Geopoint(latitude=lat, longitude=lon)

# 	forecast = point.get_weather()
# 	#print(forecast)

# 	# Set the popup info; sample tuple = ('2021-02-04 03:00:00', 31.71, 'clear sky', '01n')
# 	# popup_content = f"""
# 	# {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
# 	# <hr style="margin:1px">
# 	# {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
# 	# <hr style="margin:1px">
# 	# {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
# 	# <hr style="margin:1px">
# 	# {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
# 	# <hr style="margin:1px">
# 	# """

# 	popup_content = ""
# 	for index,item in enumerate(forecast,0):
# 		popup_content = popup_content + f'{forecast[index][0][-8:-6]}h: {round(forecast[index][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[index][-1]}@2x.png" width=35><hr style="margin:1px">'
		
# 	print(popup_content)

# 	content = ""
# 	popup_content = popup_content.replace("03h", "3 AM", 3)
# 	popup_content = popup_content.replace("06h", "6 AM", 3)
# 	popup_content = popup_content.replace("09h", "9 AM", 3)
# 	popup_content = popup_content.replace("12h", "12 PM", 3)
# 	print(popup_content)



# 		# hour = item[0][-8:-6]
# 		# if int(hour) == 12:
# 		# 	print(str(hour) + " PM")
# 		# elif (int(hour) > 12 and int(hour) <= 21):
# 		# 	print(str(int(hour) - 12) + " PM")
# 		# else:
# 		# 	print(str(hour) + " AM")
		

# 	#popup = Popup(str(point.get_weather()), parse_html=True)
# 	popup = Popup(popup_content, max_width=400)
# 	popup.add_to(point)

# 	point.add_to(mymap)


mymap.save(file_loc)
webbrowser.open(file_loc)
