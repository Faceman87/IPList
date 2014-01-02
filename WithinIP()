#geoIP database creator
#Created by: Christopher Gaines
#Created on: 10/16/2013
#Modified on: 10/28/2013

import sqlite3, os, re, time, sys, logging, datetime, fileinput, subprocess

#SEE BOTTOM for INITIALIZERS

#=====================================================================================================================	
#    	IS IP "WITHIN RANGE" FUNCTION
#=====================================================================================================================	
def withinIP():
	maxBit = 254
	testIP = "71.54.37.7"
	#testRange = "10.0.0.0-10.1.2.3"
	testRange = "71.54.36.253-71.54.37.7"
	splitIP = testRange.split("-")
	print(testIP)
	print(testRange)
	#Now store each IP as a string
	IPstart = splitIP[0]
	IPend = splitIP[1]

	#Convert this string to an integer list
	testIP = testIP.split(".")
	for O in range(0, 4):
		testIP[O] = int(testIP[O])
	
	#Convert this string to an integer list
	splitIPstart = IPstart.split(".")
	for O in range(0, 4):
		splitIPstart[O] = int(splitIPstart[O])
		
	#Convert this string to an integer list
	splitIPend = IPend.split(".")
	for O in range(0, 4):
		splitIPend[O] = int(splitIPend[O])
		
	isTrue = False
	
	#Case 1 (A<T<B)
	if (splitIPstart[0] < testIP[0] < splitIPend[0]):
		if(testIP[1] <= maxBit and testIP[2] <= maxBit and testIP[3] <= maxBit):
			isTrue = True
			print("HIT #1")
	
	#Case 2 (A=T=B)
	elif (splitIPstart[0] == testIP[0] == splitIPend[0]):
		if (splitIPstart[1] < testIP[1] < splitIPend[1] and testIP[2] <= maxBit and testIP[3] <= maxBit):
			isTrue = True
			print("HIT #2")
		elif (splitIPstart[1] == testIP[1] < splitIPend[1] and splitIPstart[2] <= testIP[2] <= maxBit and splitIPstart[3] <= testIP[3] <= maxBit):
			isTrue = True
			print("HIT #3")
		elif (splitIPstart[1] < testIP[1] == splitIPend[1] and testIP[2] < splitIPend[2] and testIP[3] <= maxBit):
			isTrue = True
			print("HIT #4")
		elif (splitIPstart[1] < testIP[1] == splitIPend[1] and testIP[2] == splitIPend [2] and testIP[3] <= splitIPend[3]):
			isTrue = True
			print("HIT #5")
		
		
	#Case 4 (A=T<B)
	elif (splitIPstart[0] == testIP[0] < splitIPend[0]):
		if (splitIPstart[1] <= testIP[1] <= maxBit and splitIPstart[2] <= testIP[2] <= maxBit and splitIPstart[3] <= testIP[3] <= maxBit):
			isTrue = True
			print("HIT #6")
		
	#case 5 (A<T=B)
	elif (splitIPstart[0] < testIP[0] == splitIPend[0]):
		if (testIP[1] < splitIPend[1] and testIP[2] <= maxBit and testIP[3] <= maxBit):
			isTrue = True
			print("HIT #7")
		elif (testIP[1] == splitIPend[1] and testIP[2] < splitIPend[2] and testIP[3] <= maxBit):
			isTrue = True
			print("HIT #8")
		elif (testIP[1] == splitIPend[1] and testIP[2] == splitIPend[2] and testIP[3] <= splitIPend[3]):
			isTrue = True
			print("HIT #9")
					
	if(isTrue == True):
		print("Within Range")
	else:
		print("Not Within Range")
		


#=====================================================================================================================	
#    	START HERE
#=====================================================================================================================	

withinIP()
