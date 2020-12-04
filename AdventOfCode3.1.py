##Processing Data ##
with open('./slopeMapInput.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()    
data = [x.replace('\n',"") for x in data]

##Code Challenge ##

right =0
down =0
trees = ''
while down < len(data):
    index=right%len(data[0])
    landed = data[down][index]
    trees = trees + landed
    right+=3
    down+=1
    count+=1
    