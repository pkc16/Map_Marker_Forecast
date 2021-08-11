# Map_Marker_Forecast
Python 3 application which plots given location on map and gives simple popup weather forecast.

Application is a command line interface which takes a user-specified location and plots it on a map and provides a popup box with a simple weather forecast.  Map is saved as an .html file.  Application uses sunnyday library, which is based on data from https://openweathermap.org.  An api key must be specified in the MapMarkerForecast_config.txt file; the key can be obtained from the website by signing up for a free account.

The output location of the map is also specifiable in the config file.

#### External Libraries used
- folium
- geopy
- pytz
- sunnyday
- timezonefinder
- webbrowser


## Author
Peter Chung
