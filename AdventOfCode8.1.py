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

def validate(data):
    already_ran= []
    iterator = 0
    acc=0
    while x:
        inst, num = data[iterator]
        if inst == "jmp" :
            already_ran.append(iterator)
            iterator+=int(num)
        elif inst == "acc": 
            already_ran.append(iterator)
            acc += int(num)
            iterator+=1
        elif inst == "nop":
            iterator+=1
        if iterator in already_ran: 
            break
    return [acc, x]

    print("Solution is: {}".format(validate(new_data)))