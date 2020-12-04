import re
with open('./passports.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]

clean_data=[]
entry = ''
for i in range(len(data)-1):
    if data[i]=='':
        clean_data.append(entry)
        entry = ''
    entry = entry+data[i]

validation_regex = ['byr:', 'iyr:', 'eyr:','hgt:','hcl:','ecl:','pid:']
count = 0


for passport in clean_data:
    validation = 0
    for thing in validation_regex:
        if re.search(thing,passport)!= None:
            validation+=1
    if validation == len(validation_regex):
        count+=1

print(count)
    
