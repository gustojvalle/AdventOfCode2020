from itertools import combinations
with open('./input1_2AdventOfCode.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()

data = [x.replace('\n','') for x in data]
data = [int(x) for x in data]


comb = combinations(data, 3)

for entry in comb:
    if sum(entry)==2020:
        print(entry[0]*entry[1]*entry[2])