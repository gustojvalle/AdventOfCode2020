with open('./answers.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]

counter = 0
clean_data=[]
entry = ''
for i in range(len(data)):
    entry = entry+data[i]
    if data[i]=='' or counter== len(data)-1:
        clean_data.append(entry)
        entry = ''
    counter+=1

##puzzle in a one liner##
total = sum([len(set(answers)) for answers in clean_data])
print(total)