from itertools import combinations
with open('./cyphers.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [int(x.replace('\n',"")) for x in data]

preamble = 25
for i in range(2,len(data)-1):
    sum_of_pairs = [sum(pair) for pair in combinations(data[:i], 2)]
    
    if i>preamble and data[i] not in sum_of_pairs:
        print("Your answer is: {}, and the Index is: {}".format(data[i], i))
        break
