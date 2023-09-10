"""
Adam Rodgers,  8/26/2023
This file stores all the code for the hierarchy. 
It holds a base class with two operator overloads

There are three derived classes with three diffrent forecasters:
	-A forecaster that trusts the weather prediction too much
    -A forecaster that distrusts the weather prediction too much
    -A neutral forecaster
    
Each tone has three functions that the user can chose from:
    -A forecast_weather function that shows the user a 10 day forecast with commentary
    -A suggest_clothing function that suggests to the user how warm to dress
    -A suggest_activity function that suggest to the user what activity to do for the day
"""

import os
import fileinput
import numpy as np


"""
Base Class for the hierarchy
"""
class base():
		#constructor 
		def __init__(self, forecast, temps):
			self._forecast = forecast
			self._temps = temps
		
		def show__forecast(self): #simple display
			print("        Average Temp | High | Low | Date | Conditions\n")
			for line in self._forecast:
				print(line)

		def __eq__(self, source):#== operator overload
			if isinstance(source, base):
				return len(self._forecast) == len(source._forecast)
			return False

		def __ne__(self, source):#!= operator overload
			if isinstance(source, base):
				return len(self._forecast) != len(source._forecast)
			return True
		


"""
Neutral tone derived class
"""
class neutral(base):

	def __init__(self, _forecast, _temps): # constructor 
		super().__init__(_forecast, _temps)

	def forecast_weather(self): #forecast weather for 10 days 
		try:
			i = 0
			while i < 10: #loop to forecast 10 days
				print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
				print(i, ": " )
				print("        This is our forecast for the day \n        ", self._forecast[i]) 
				if(self._temps[i] >= 95): #changes output depending on temphanges output depending on temp
					print("        It is a very hot day, try to avoid sunburn and keep yourself cool")
				elif(self._temps[i] >= 85):
					print("        It is a hot day try to keep cool out there")
				elif(self._temps[i] >= 65):
					print("        The weather is pleasent")
				elif(self._temps[i] >= 55):
					print("        It is cold out there, make sure to stay warm")
				elif(self._temps[i] < 55):
					print("        It is very cold out there, make sure to stay warm")
				i += 1
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False
			

	def suggest_clothes(self, i): # suggests clothing for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        It is a very hot day, make sure to dress light and protect your skin")
			elif(self._temps[i] >= 85):
				print("        It is a hot day dress lightly")
			elif(self._temps[i] >= 65):
				print("        The weather is pleasent, dress how ever you would like")
			elif(self._temps[i] >= 55):
				print("        It is cold out there, make sure to have a few extra layers")
			elif(self._temps[i] < 55):
				print("        It is very cold out there, make sure to wear winter clothing")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False

	def suggest_activity(self, i):# suggests activity for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        It is a very hot day, maybe going for a swim in a cold lake will help")
			elif(self._temps[i] >= 85):
				print("        I suggest going to mt. hood its very cool at the top")
			elif(self._temps[i] >= 65):
				print("        The weather is pleasent, its a perfect day for a picnic")
			elif(self._temps[i] >= 55):
				print("        Go on a hike to warm up")
			elif(self._temps[i] < 55):
				print("        make a campfire and warm up")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False

	
"""
Cynical tone derived class
"""
class cynical(base):

	def __init__(self, _forecast, _temps): # constructor 
		super().__init__(_forecast, _temps)

	def forecast_weather(self): #forecast weather for 10 days 
		try:
			i = 0
			while i < 10:
				print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
				print(i, ": " )
				print("        This is our forecast for the day \n        ", self._forecast[i])
				if(self._temps[i] >= 95): #changes output depending on temp
					print("        They claim it is going to be a very hot day  but its probably going to be cold")
				elif(self._temps[i] >= 85):
					print("        its supposedly a hot day ")
				elif(self._temps[i] >= 65):
					print("        The weather is appraently going to be pleasent ...so its probably going to be thunder storms")
				elif(self._temps[i] >= 55):
					print("        They say its going to be cold but they are always wrong!")
				elif(self._temps[i] < 55):
					print("        They claim it is going to be very cold and \"to be carful\" but i say live your life")
				i += 1
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False


	def suggest_clothes(self, i):# suggests clothing for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        They say its going to be very hot so probably dress like winter")
			elif(self._temps[i] >= 85):
				print("        dress like its cold out just to be safe!")
			elif(self._temps[i] >= 65):
				print("        apparently The weather is pleasent, but they are probably wrong so bring an umbrella")
			elif(self._temps[i] >= 55):
				print("        they say its going to be cold so dress like summer!")
			elif(self._temps[i] < 55):
				print("        The weather model says its going to be really cold but I say its going to be a perfect day for shorts")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False

	def suggest_activity(self, i):# suggests activity for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        Theoretically its a hot day but I suggest warming up with a campfire")
			elif(self._temps[i] >= 85):
				print("        That means its porbably going to be a coll day for a hike")
			elif(self._temps[i] >= 65):
				print("        The weather is pleasent, its a perfect day for a picnic...in the snow...")
			elif(self._temps[i] >= 55):
				print("        I hear mt.hood is good in the \"heat\"")
			elif(self._temps[i] < 55):
				print("        It going to be very cold they say so i say go for a swim in the lake")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False


"""
Trusting tone derived class
"""
class trusting(base):

	def __init__(self, _forecast, _temps):# constructor 
		super().__init__(_forecast, _temps)

	def forecast_weather(self):#forecast weather for 10 days 
		try:
			i = 0
			while i < 10:
				print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
				print(i, ": " )
				print("        This is our  GUARANTEED forecast for the day \n        ", self._forecast[i])
				if(self._temps[i] >= 95): #changes output depending on temp
					print("        It is deffinetly going to be a very hot day!")
				elif(self._temps[i] >= 85):
					print("        It will be a hot day without doute!")
				elif(self._temps[i] >= 65):
					print("        The weather WILL be great this day")
				elif(self._temps[i] >= 55):
					print("        It UNQUESTIONABLY will be cold")
				elif(self._temps[i] < 55):
					print("        It is going to ber VERY COLD FOR SURE!")
				i += 1
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False

	def suggest_clothes(self, i):# suggests clothing for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        It will be a very hot day, make sure to dress light and protect your skin. Do NOT dress warmly!")
			elif(self._temps[i] >= 85):
				print("        Its a hot day GUARANTEED so dress lightly")
			elif(self._temps[i] >= 65):
				print("        The weather is pleasent, and it will STAY like that so dress how you like")
			elif(self._temps[i] >= 55):
				print("        It WILL BE cold out there, make sure to have a few extra layers")
			elif(self._temps[i] < 55):
				print("        It is UNQUESTIONABLY COLD OUT THERE dress very warmly!")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False
		

	def suggest_activity(self, i):# suggests activity for inputed day 
		try:
			print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
			if(self._temps[i] >= 95): #changes output depending on temp
				print("        It is DIFFINITELY a very hot day, going for a swim in a cold lake will help!")
			elif(self._temps[i] >= 85):
				print("        Go to mt. hood its very cool at the top!")
			elif(self._temps[i] >= 65):
				print("        The weather is pleasent the ENTIRE day, its a perfect day for a picnic")
			elif(self._temps[i] >= 55):
				print("        Going on a hike WILL warm you up!")
			elif(self._temps[i] < 55):
				print("        Stay inside, it too COLD to go outside!")
			return True
		except:
			print("\n <AN ERROR OCCURED> \n")
			return False