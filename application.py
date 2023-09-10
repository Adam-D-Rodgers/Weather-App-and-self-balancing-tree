"""
Adam Rodgers,  8/26/2023

This file holds the code for the application part of this program.
It takes in a file with weather data and stores it all in a list. 
It then takes the data and stores the avarage temp for each day in a numpy list.
"""

import os
import fileinput
import numpy as np
from hierarchy import base
from hierarchy import neutral
from hierarchy import cynical
from hierarchy import trusting

class application():
	def __init__(self): #constructor 

		self.__choices = list()

		with open("info.txt", "r") as file: #Opens the file and stores the data in list and numpy
			self.__forecast = file.readlines()
		self.__temps = np.array([], dtype = float)
		with open("info.txt", "r") as file:
			for line in file:
				line = line.strip()
				if "°" in line:
					part = line.split("°")
					temp = float(part[0])
					self.__temps = np.append(self.__temps, temp)

		#self.neutral_tone = neutral(self.__forecast, self.__username) exception handling test
		self.neutral_tone = neutral(self.__forecast, self.__temps)
		self.cynical_tone = cynical(self.__forecast, self.__temps)
		self.trusting_tone = trusting(self.__forecast, self.__temps)
		pass

	def menu(self): #Menu function to allow user to chose tone
		option = 0
		print("\nOptions: " )
		print("       1: A neutral tone")
		print("       2: A very cynical tone")
		print("       3: A very trusting tone")
		option = input("What Tone Would You Like: ")
		if(option ==  "1"): 
			self.__choices.append("Neutral")
			return 1
		elif(option == "2"):
			self.__choices.append("Cynical")
			return 2
		elif(option == "3"):
			self.__choices.append("Trusting")
			return 3
		else:
			print("Please Enter Valid Input")
			return self.menu()
			
		
	def function_menu(self, tone): #Menu function to allow user to chose what function to call
		option = 0
		while option != "4": #loop to allow for mutiple choices
			print("\nWhat Function Would you like to run: " )
			print("       1: A 10 day weather forecast with commentary")
			print("       2: Suggest clothing for a day")
			print("       3: Suggest activity for a day")
			print("       4: Exit Weather App")
			option = input("What option would you like: ")
			if(option == "1"): #simple choice menu, runcs the code depending on user choice
				try:
					self.__choices.append("10 Day Forecast")
					tone.forecast_weather()
				except:
					print("\n <AN ERROR OCCURED> \n")
			elif(option == "2"):
				day = int(input("What day would you like a suggestion for? (please enter from 0-9): " ))
				try:
					self.__choices.append("Suggest Clothes")
					tone.suggest_clothes(day)
				except:
					print("\n <AN ERROR OCCURED> \n")
			elif(option == "3"):
				day = int(input("What day would you like a suggestion for? (please enter from 0-9): " ))
				try:
					self.__choices.append("Suggest Activity")
					tone.suggest_activity(day)
				except:
					print("\n <AN ERROR OCCURED> \n")
			elif(option != "4"):
				print("Please Enter Valid Input")

	def run(self): # This function runs the application
	
		print("\nWelcome To The Tone Weather App \n Here we allow you to chose from three options of tone on how you want your weather to be forecasted!\n")
		option = self.menu()
		if(option == 1): #runcs the code depending on user choice
			self.neutral_tone.forecast_weather()
			self.function_menu(self.neutral_tone)
		elif(option == 2):
			self.cynical_tone.forecast_weather()
			self.function_menu(self.cynical_tone)
		elif(option == 3):
			self.trusting_tone.forecast_weather()
			self.function_menu(self.trusting_tone)
		return self.__choices
