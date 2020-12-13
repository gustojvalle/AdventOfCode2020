from itertools import combinations
with open('./jolts.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [int(x.replace('\n',"")) for x in data]
data.append(max(data)+3)

data = sorted(data)

max_jolts = data[-1]
i =[1]	+[0]*max_jolts + [0, 0 ]
for r in data: 
	i[r]=i[r-1]+ i[r-2]+i[r-3]
	if r == max_jolts: 
		print("your answer is: {}".format(i[r]))
		break