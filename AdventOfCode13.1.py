from datetime import datetime
import re	
import math
with open('./busesTest.txt') as file:
    my_input = file
    data=[line.replace('\r\n', '')  for line in file.readlines()]
    file.close()

time_of_departure = int(data[0]) 
buses = [int(bus) for bus in data[1].split(',') if bus != "x"]
diff = [-time_of_departure%x for x in buses]
time_diff = min(diff)
bus_id = buses[diff.index(time_diff)]


print("Answer part 1 is: {}".format(time_diff*bus_id))
