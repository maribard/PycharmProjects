# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyowm
from pyowm.utils.config import get_default_config
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

config_dict = get_default_config()
config_dict['language'] = 'pl'

owm = pyowm.OWM('1bcf2eb78e2d9046074621673137271a', config_dict)
mgr = owm.weather_manager()

miasto = input("Podaj miasto: ")

observation = mgr.weather_at_place(miasto)
w = observation.weather
temp = w.temperature('celsius')["temp"]
print("W mieście " + miasto + " " + w.detailed_status + " i " + str(temp) + " stopni")