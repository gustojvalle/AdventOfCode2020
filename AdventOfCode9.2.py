from itertools import combinations
with open('./cyphers.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [int(x.replace('\n',"")) for x in data]


number = data[662]
print(number)
new_data = data[:663]


for i in range(2,len(data)-1):
	for j in range(1,len(data)-1):
		rang = new_data[i:j]
		sums =  sum(rang)
		if number == sums and number not in rang:
			print("min: {}, max: {}".format(min(rang), max(rang)))
			print("Answer is: {}".format(min(rang) + max(rang)))
			break

