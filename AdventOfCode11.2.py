from datetime import datetime	
with open('./seats.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()


def split(word): 
	return [char for char in word]
import copy




data = [split(line.replace("\r", "").replace('\n', '')) for line in data]
copy_data = copy.deepcopy(data)
movmts= {0:['#'],1:copy_data}
print(len(movmts))
x=1
times = datetime.now()
while [item for sublist in movmts[x-1] for item in sublist].count('#') != [item for sublist in movmts[x] for item in sublist].count('#'):
	print("X: lgkgkjhgkjhgkjhgkjhgkjhgkhjgkjhgkjhgkjhgkjhgjhghj", x)
	new_seat_map = copy.deepcopy(movmts[x])
	for i in range(len(data)): 
		for j in range(len(data[i])):
			one = [i+1, j]
			two = [i-1, j]
			three =[i, j+1]
			four = [i, j-1]
			five = [i+1, j+1]
			six = [i+1, j-1]
			seven = [i-1, j+1]
			eight = [i-1, j-1]
			z=0
			v=0
			print("hi")
			while movmts[x][i+z][j] == '.' and z+i < len(data)-1:
				
				one == [i+z, j]
				z+=1

			z=0
			v=0
			while movmts[x][i+z][j]=='.' and z+i < len(data)-1:

				two == [i-z, j]
				z+=1
			z=0
			v=0
			while movmts[x][i][j+z]=='.' and z+j < len(data[0])-1:
				print(i, j)
				three == [i, j+z]
				z+=1
			z=0
			v=0
			while movmts[x][i][j-z]=='.' and z+j < len(data[0])-1:
				four == [i, j-z]
				z+=1
			z=0
			v=0
			while movmts[x][i+v][j+z]=='.' and z+j < len(data[0])-1 and v+i< len(data)-1:
				five == [i+v, j+z]
				z+=1
				v+=1
			z=0
			v=0
			
			while movmts[x][i+v][j-z]=='.' and z+j < len(data[0])-1 and v+i< len(data)-1:
				six == [i+v, j-z]
				z+=1
				v+=1
			z=0
			v=0
			
			while movmts[x][i-v][j+z]=='.' and z+j < len(data[0])-1 and v+i< len(data)-1:
				seven == [i-v, j+z]
				z+=1
				v+=1
			z=0
			v=0

			while movmts[x][i-v][j-z]=='.' and z+j < len(data[0])-1 and v+i< len(data)-1:
				eight == [i-v, j-z]
				z+=1
				v+=1
			

			print(one)


			



			adjacent_seats = [one, two, three, four, five, six, seven]
			print(adjacent_seats	)
			adjacent_seats = [seat  for seat in adjacent_seats if (seat[0]<len(data) and seat[1]< len(data[0]) and seat[0]>=0 and seat[1]>=0)]
			adjacent_seats = [movmts[x][k][l] for k,l in adjacent_seats] 		
			if adjacent_seats.count('#')==0 and movmts[x][i][j]=='L':
				new_seat_map[i][j] = '#'
			elif movmts[x][i][j] == '#' and adjacent_seats.count('#')>=5: 
				new_seat_map[i][j] = 'L'
	x+=1
	movmts[x] = new_seat_map
print("answer is: {}".format([item for sublist in movmts[x] for item in sublist].count('#')))
print(datetime.now() - times)