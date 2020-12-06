
##getting the data
with open('./answers.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]

##Preparing data and solving the puzzle
clean_data=[]
total=0
for i in range(len(data)): 
    if entry != data[i] and data[i]!='':
        entry = set(data[i]).intersection(entry)
    if data[i]=='' or i == len(data)-1:
        total += len(entry)
        if i < len(data)-1:
            entry = data[i+1]   
print(total)