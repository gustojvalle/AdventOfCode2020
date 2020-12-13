from itertools import combinations
from datetime import datetime	
import time
with open('./seats.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
def split(word): 
	return [char for char in word]
import copy


def printing(data):
	for line in data: 
		print(line)




data = [split(line.replace("\r", "").replace('\n', '')) for line in data]
copy_data = copy.deepcopy(data)
movmts= {0:['#'],1:copy_data}
print(len(movmts))
x=1
times = datetime.now()
while [item for sublist in movmts[x-1] for item in sublist].count('#') != [item for sublist in movmts[x] for item in sublist].count('#'):
	new_seat_map = copy.deepcopy(movmts[x])
	for i in range(len(data)): 
		for j in range(len(data[i])):
			adjacent_seats = [[i+1,j], [i-1, j], [i, j+1], [i, j-1], [i+1, j+1], [i-1, j-1], [i+1, j-1], [i-1, j+1]]
			adjacent_seats = [seat  for seat in adjacent_seats if (seat[0]<len(data) and seat[1]< len(data[0]) and seat[0]>=0 and seat[1]>=0)]
			adjacent_seats = [movmts[x][k][l] for k,l in adjacent_seats] 		
			if adjacent_seats.count('#')==0 and movmts[x][i][j]=='L':
				new_seat_map[i][j] = '#'
			elif movmts[x][i][j] == '#' and adjacent_seats.count('#')>3: 
				new_seat_map[i][j] = 'L'
	x+=1
	movmts[x] = new_seat_map
	printing(movmts[x])
	time.sleep(1)
print("answer is: {}".format([item for sublist in movmts[x] for item in sublist].count('#')))
print(datetime.now() - times)