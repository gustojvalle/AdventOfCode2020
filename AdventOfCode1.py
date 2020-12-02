with open('./input1AdventOfCode.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n','') for x in data]
data = [int(x) for x in data]

x = 0
while len(data)> 0:
    x = data.pop()
    for entry in data:
        if x+entry == 2020:
            print(x*entry)
            break