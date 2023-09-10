"""
Adam Rodgers,  8/26/2023
This program a weather applicatioon in which you can choose the tone of your weather forecaster. 
The three options are:
    -A forecaster that trusts the weather prediction too much
    -A forecaster that distrusts the weather prediction too much
    -A neutral forecaster

Each tone has three functions that the user can chose from:
    -A forecast_weather function that shows the user a 10 day forecast with commentary
    -A suggest_clothing function that suggests to the user how warm to dress
    -A suggest_activity function that suggest to the user what activity to do for the day

The program takes in weather forcast data and stores it in a list and a numpy array.  

"""
import os
import fileinput
from application import application
from tree import AVL

test = AVL() #Just calls the tree
option = 0
while option != "4": #loop to allow for mutiple choices
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("What yould you like to do?")
    print("       1: New User")
    print("       2: Search User")
    print("       3: Display Users")
    print("       4: Exit Weather App")
    option = input("What option would you like: ")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    if(option == "1"): #simple choice menu, runs the code depending on user choice
        test.load()
    elif(option == "2"):
        search = input("What user would you like to search: " )
        test.retrieve(search)
    elif(option == "3"):
        test.display()
    elif(option != "4"):
        print("Please Enter Valid Input")
				
