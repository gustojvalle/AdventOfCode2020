from datetime import datetime
import re	
import math
with open('./buses.txt') as file:
    my_input = file
    data=[line.replace('\r\n', '')  for line in file.readlines()]
    file.close()


buses = [int(bus) if bus != "x" else 0 for bus in data[1].split(',') ]
bus_no_x = [bus for bus in buses if bus!= 0 ]
bus_constraint = {}

for bus, indice in zip(buses, range(len(buses))): 
	if bus!=0: 
		bus_constraint[bus]= indice
step = 1
number = 0
for bus in bus_no_x:
	while number%bus != ((bus-bus_constraint[bus])%bus):
		number+=step
	step*=bus

print("Answer for part 2 is: "+ str(number))
	


