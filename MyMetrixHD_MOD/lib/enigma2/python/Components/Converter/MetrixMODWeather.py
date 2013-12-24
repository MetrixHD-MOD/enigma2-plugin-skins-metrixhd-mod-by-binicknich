#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#######################################################################
#
#    MetrixMODWeather for Enigma2
#    Coded by iMaxxx (c) 2013
#    Support: www.vuplus-support.com
#
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
#
#######################################################################
from Components.Converter.Converter import Converter
from Components.config import config, ConfigText, ConfigNumber, ConfigDateTime
from Components.Element import cached

class MetrixMODWeather(Converter, object):
	
	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = type
			
	@cached
	def getText(self):
		try:
			if self.type == "currentLocation":
				return config.plugins.MetrixMODWeather.currentLocation.value
			if self.type == "currentWeatherTemp":
				return config.plugins.MetrixMODWeather.currentWeatherTemp.value
			elif self.type == "currentWeatherText":
				return config.plugins.MetrixMODWeather.currentWeatherText.value
			elif self.type == "currentWeatherCode":
				return config.plugins.MetrixMODWeather.currentWeatherCode.value
			elif self.type == "forecastTodayCode":
				return config.plugins.MetrixMODWeather.forecastTodayCode.value
			elif self.type == "forecastTodayTempMin":
				return config.plugins.MetrixMODWeather.forecastTodayTempMin.value + " " + self.getCF()
			elif self.type == "forecastTodayTempMax":
				return config.plugins.MetrixMODWeather.forecastTodayTempMax.value + " " + self.getCF()
			elif self.type == "forecastTodayText":
				return config.plugins.MetrixMODWeather.forecastTodayText.value
			elif self.type == "forecastTomorrowCode":
				return config.plugins.MetrixMODWeather.forecastTomorrowCode.value
			elif self.type == "forecastTomorrowTempMin":
				return config.plugins.MetrixMODWeather.forecastTomorrowTempMin.value + " " + self.getCF()
			elif self.type == "forecastTomorrowTempMax":
				return config.plugins.MetrixMODWeather.forecastTomorrowTempMax.value + " " + self.getCF()
			elif self.type == "forecastTomorrowText":
				return config.plugins.MetrixMODWeather.forecastTomorrowText.value
			elif self.type == "title":
				return self.getCF() + " | " + config.plugins.MetrixMODWeather.currentLocation.value
			elif self.type == "CF":
				return self.getCF() 
			else:
				return ""
		except:
			return ""
		
		
	def getCF(self):
		if config.plugins.MetrixMODWeather.tempUnit.value == "Fahrenheit":
			return "°F"
		else: 
			return "°C"
		

	text = property(getText)