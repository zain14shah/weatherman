"""
Generating reports of temperature from given text files.
"""

import os
file_list = os.listdir('./weatherdata/')
hottest_day = {}
hottest_date = {}
coldest_day = {}
maxi_humidity= {}
mini_humidity= {}

for file_name in file_list:

	with open('weatherdata/' + file_name) as f:
		lines = f.read().splitlines()[2:-1]
		for line in lines:
			line = line.split(',')
			year = line[0].split('-')[0]
			date = line[0]
			try:
				max_temp = int(line[1])
				min_temp = int(line[3])
				max_humid= int(line[7])
				min_humid = int(line[9])
			except ValueError:
				continue
			#Temp
			hottest_day[year] = hottest_day.get(year, -99)
			hottest_date[year] = hottest_date.get(year,'DATE')
			if max_temp > hottest_day[year]:
				hottest_day[year] = max_temp
				hottest_date[year] = date 
			#min_temp
			hottest_day[year] = hottest_day.get(year, 999)
			if min_temp < hottest_day[year]:
				hottest_day[year] = min_temp
			#max_humid
			maxi_humidity[year] = maxi_humidity.get(year, -99)
			if max_humid > maxi_humidity[year]:
				maxi_humidity[year] = max_humid
				
			#min_humid
			mini_humidity[year] = mini_humidity.get(year, 999)
			if min_humid < mini_humidity[year]:
				mini_humidity[year] = min_humid

"""
print("Year		MAX Temp	MIN Temp	MAX Humidity	MIN Humidity")
i=1996				
while i < 2012:	
	print(i,"		",hottest_day[str(i)],"		",coldest_day[str(i)],"		",maxi_humidity[str(i)],"		",mini_humidity[str(i)])
	i += 1
print("")
print("")
print("")
print("")  
print("Year		MAX Temp	DATE")
i=1996				
while i < 2012:	
	print(i,"		",hottest_day[str(i)],"		",hottest_date[str(i)])
	i += 1
"""
print(hottest_day)
