from datetime import datetime
import re	
import math
with open('./coord.txt') as file:
    my_input = file
    data=[line.replace('\r\n', '')  for line in file.readlines()]
    file.close()

strong = datetime.now()
N_S_E_W = {'N':1, 'S':-1 , 'E':1, 'W':-1, 'R':1, 'L': -1}

def turn_ship(curr_pos, direction, degree):
	r= ['N', 'E', 'S', 'W']
	return r[(r.index(curr_pos)+degree/90*N_S_E_W[direction])%4]

data = [[re.search(r'[A-Z]', coord).group(),int( re.search(r'[0-9]+', coord).group())] for coord in data]


N_S = 0
E_W = 0
pos = 'E'
for coord in data:
	 

	direction = coord[0] 


	if direction == 'F': 
		direction = pos
		if direction == 'N' or direction == 'S': 
			N_S += coord[1]*int(N_S_E_W[direction])
		elif direction == 'W' or direction == 'E':
			E_W += coord[1]*int(N_S_E_W[direction])

	elif direction == 'R' or direction == 'L':
		pos = turn_ship(pos, direction, coord[1])


	if coord[0] == 'N' or coord[0] == 'S': 
		N_S += coord[1]*int(N_S_E_W[direction])
	elif coord[0] == 'W' or coord[0] == 'E':
		E_W += coord[1]*int(N_S_E_W[direction])

print((datetime.now()-strong)*1000)
print("N_S, E_W,", N_S, E_W)
print("Total is: ",  math.sqrt(N_S**2) + math.sqrt(E_W**2))