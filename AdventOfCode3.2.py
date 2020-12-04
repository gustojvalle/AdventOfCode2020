##Processing Data ##
with open('./slopeMapInput.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()    
data = [x.replace('\n',"") for x in data]

##Code Challenge ##
slopes = [tuple([1,1]),tuple([3,1]),tuple([5,1]),tuple([7,1]),tuple([1,2])]
multiplication = 1

for slope in slopes: 
    right =0
    down =0
    trees = ''
    while down < len(data):
        index=right%len(data[0])
        path = data[down][index]
        trees = trees + path
        right+=slope[0]
        down+=slope[1]
    multiplication = multiplication*trees.count("#")
    
print(multiplication)
    