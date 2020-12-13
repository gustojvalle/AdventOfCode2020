from datetime import datetime
import re	
import math
with open('./coord.txt') as file:
    my_input = file
    data=[line.replace('\r\n', '')  for line in file.readlines()]
    file.close()

strong = datetime.now()
def turn_ship(way_point, degree, direction):
	
	if (degree == 90 and direction == 'R') or (degree == 270 and direction == 'L'): 
		return {'N':way_point['W'],'S':way_point['E'], 'W':way_point['S'], 'E':way_point['N'] }	
	elif (degree == 270 and direction == 'R') or (degree == 90 and direction == 'L'): 
		return {'N':way_point['E'],'S':way_point['W'], 'W':way_point['N'], 'E':way_point['S'] }	
	elif degree == 180:
		return {'N':way_point['S'],'S':way_point['N'], 'W':way_point['E'], 'E':way_point['W'] }		





data = [[re.search(r'[A-Z]', coord).group(),int( re.search(r'[0-9]+', coord).group())] for coord in data]


N = 0 
S = 0
W = 0
E = 0 
way_pnt = {'N':1, 'S':0, 'W':0, 'E': 10}
for coord in data:
	if coord[0] == 'F': 
		N += way_pnt['N']*coord[1]
		S += way_pnt['S']*coord[1]
		E += way_pnt['E']*coord[1]
		W += way_pnt['W']*coord[1]
	elif coord[0] == 'R' or coord[0]== 'L':
		way_pnt = turn_ship(way_pnt, coord[1], coord[0])
			
	if coord[0] == 'N': 
		way_pnt['N'] = way_pnt['N']+coord[1]
	elif coord[0] == 'S': 
		way_pnt['S'] = way_pnt['S']+coord[1] 
	elif coord[0] == 'W': 
		way_pnt['W'] = way_pnt['W']+coord[1]
	elif coord[0] == 'E':
		way_pnt['E'] = way_pnt['E']+coord[1]

print((datetime.now()-strong))
print("Total is: ",  abs(N-S) + abs(E-W))