from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty

gps_location = StringProperty()
gps_status = StringProperty('Click Start to get GPS location updates')