
##preparing data ##
with open('./instruction.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]

new_data={}
i=0 
for entry in data: 
    new_data[i]=entry.split(" ")
    i+=1


##Solving Puzzle
def validate(data, index, modification):
    already_ran= []
    iterator = 0
    acc=0
    inst = ""
    num = 0
    while True:
        if iterator in already_ran or  iterator<0: 
            return [False, acc]
        already_ran.append(iterator)
        if int(iterator) == int(index):
            inst, num == modification
        else:
            if iterator> len(data)-1:
                return [True, "your Asnswer: {}".format(acc)]
            inst, num = data[iterator]
        
        if inst == "jmp" :
            iterator+=int(num)-1
        elif inst == "acc": 
            acc += int(num)
        elif inst == "nop":
            pass
        iterator+=1
    return [False, acc]

for i in range(len(new_data)):
    if new_data[i][0] == "jmp":
        trying = ['nop', 0]
    elif new_data[i][0]== 'nop':
        trying = ['jmp', new_data[i][1]]
    
    d = validate(new_data,i, trying)
    if d[0]: 
        print(str(d))
        break 
