#geoIP database creator
#Created by: Christopher Gaines
#Created on: 10/16/2013
#Modified on: 05/09/2014

import sqlite3, os, re, time, sys, logging, datetime, fileinput, subprocess


#=====================================================================================================================	
#    	LIST ALL IP FUNCTION
#=====================================================================================================================			
def listIPs(testRange):
	maxBit = 255
	validIP = True
	count = 0
	
	#Separate the IPs
	splitIP = testRange.split("-")

	#Now store each IP as a string
	IPstart = splitIP[0]
	IPend = splitIP[1]

	#Convert this string to an integer list
	splitIPstart = IPstart.split(".")
	for O in range(0, 4):
		splitIPstart[O] = int(splitIPstart[O])
		
	#Convert this string to an integer list
	splitIPend = IPend.split(".")
	for O in range(0, 4):
		splitIPend[O] = int(splitIPend[O])
	
	#Test if IP is valid
	if (splitIPstart[0] == maxBit or splitIPstart[1] == maxBit or splitIPstart[2] == maxBit or splitIPstart[3] == maxBit):
		print("Invalid start IP, 255 is reserved for Network and not a valid Bit")
		validIP = False
	
	#Start timer	
	#start = datetime.datetime.now()
	#startTime = start.strftime("%H:%M:%S")
	
	#Start listing IPs
	if (validIP == True):
		
		for i in range(0, 4):

			#loop through 0-254 bits on last bit sequence
			while(splitIPstart[i] < splitIPend[i] and splitIPstart[i] < maxBit and splitIPstart[0] < maxBit and splitIPstart[1] < maxBit and splitIPstart[2] < maxBit and splitIPstart[3] < maxBit):
				writeResults = str(splitIPstart[0]) + '.' + str(splitIPstart[1]) + '.' + str(splitIPstart[2]) + '.' + str(splitIPstart[3]) + '\n'
				results.write(writeResults)
				print(writeResults)
				count = count + 1	
				
				if(splitIPstart[0] < maxBit-1 and splitIPstart[1] == maxBit-1 and splitIPstart[2] == maxBit-1 and splitIPstart[3] == maxBit-1 and i == 0):
					splitIPstart[0] = splitIPstart[0] + 1
					splitIPstart[1] = 0
					splitIPstart[2] = 0
					splitIPstart[3] = 0
					writeResults = str(splitIPstart[0]) + '.' + str(splitIPstart[1]) + '.' + str(splitIPstart[2]) + '.' + str(splitIPstart[3]) + '\n'
					results.write(writeResults)
					print(writeResults)
					count = count + 1
						
				elif(splitIPstart[1] < maxBit -1 and splitIPstart[2] == maxBit-1 and splitIPstart[3] == maxBit-1 and i <= 1):
					splitIPstart[1] = splitIPstart[1] + 1
					splitIPstart[2] = 0
					splitIPstart[3] = 0
					writeResults = str(splitIPstart[0]) + '.' + str(splitIPstart[1]) + '.' + str(splitIPstart[2]) + '.' + str(splitIPstart[3]) + '\n'
					results.write(writeResults)
					print(writeResults)
					count = count + 1
					
				elif(splitIPstart[2] < maxBit-1 and splitIPstart[3] == maxBit-1 and i <= 2):
					splitIPstart[2] =  splitIPstart[2] + 1
					splitIPstart[3] = 0
					writeResults = str(splitIPstart[0]) + '.' + str(splitIPstart[1]) + '.' + str(splitIPstart[2]) + '.' + str(splitIPstart[3]) + '\n'
					results.write(writeResults)
					print(writeResults)
					count = count + 1
				
				splitIPstart[3] = splitIPstart[3] + 1 
			#endWhile
		#endfor
	
		#Print and Count End IP If it's a proper IP
		if (splitIPend[0] != maxBit and splitIPend[1] != maxBit and splitIPend[2] != maxBit and splitIPend[3] != maxBit):
			writeResults = str(splitIPend[0]) + '.' + str(splitIPend[1]) + '.' + str(splitIPend[2]) + '.' + str(splitIPend[3]) + '\n'
			results.write(writeResults)
			print(writeResults)
			count = count + 1
		else:
			print("Invalid End IP, 255 is reserved for Network, showing last valid IP")
	
	#endif
	
	#Stop timer
	#end = datetime.datetime.now()	
	#endTime = end.strftime("%H:%M:%S")
	
	#print("Start: ", startTime)
	#print("End  : ", endTime)
	#print("Count: ", count)

#=====================================================================================================================	
#    	START HERE
#=====================================================================================================================

listFile = open("C:\\Users\\84152\\Documents\\ipSplitter\\SplitIP\\list.txt", 'r+')
results = open("C:\\Users\\84152\\Documents\\ipSplitter\\SplitIP\\results.txt", 'w')
for line in listFile:
	if re.search("-",line):
		testRange = line
		listIPs(testRange)
	else:
		print(line)
		results.write(line)
	#ENDIF
#ENDFOR
