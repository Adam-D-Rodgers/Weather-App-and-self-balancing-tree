"""
Adam Rodgers,  8/26/2023

This file stores all the test suites for the hierarchy
"""

import os
import fileinput
import numpy as np
from hierarchy import base
from hierarchy import neutral
from hierarchy import cynical
from hierarchy import trusting
import pytest


#loads all the data into array and list
with open("info.txt", "r") as file:
	forecast = file.readlines()
temps = np.array([], dtype = float)
with open("info.txt", "r") as file:
	for line in file:
		line = line.strip()
		if "°" in line:
			part = line.split("°")
			temp = float(part[0])
			temps = np.append(temps, temp)

	
#sets up for testing each class
@pytest.fixture
def setup1():
	neutral_tone = neutral(forecast, temps)
	return neutral_tone

@pytest.fixture
def setup2():
	cynical_tone = cynical(forecast, temps)
	return cynical_tone

@pytest.fixture
def setup3():
	trusting_tone = trusting(forecast, temps)
	return trusting_tone

#testing neutral class
def test_neutral(setup1: neutral):
	assert setup1.forecast_weather() == True
	assert setup1.suggest_clothes(5) == True
	assert setup1.suggest_activity(5) == True

#testing cynical class
def test_cynical(setup2: cynical):
	assert setup2.forecast_weather() == True
	assert setup2.suggest_clothes(5) == True
	assert setup2.suggest_activity(5) == True

#testing trusting class
def test_trusting(setup3: trusting):
	assert setup3.forecast_weather() == True
	assert setup3.suggest_clothes(5) == True
	assert setup3.suggest_activity(5) == True

#testing operator overloads
def test_operators():
	test_base = base(forecast, temps)
	test_base2 = base(forecast, temps)
	assert test_base == test_base2
	assert not test_base != test_base2