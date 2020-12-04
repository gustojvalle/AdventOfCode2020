
##preparing the data##
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
    
##solving challenge##

validation_regex = ['byr:[0-9]{4}', 
                    'iyr:[0-9]{4}', 
                    'eyr:[0-9]{4}',
                    'hgt:[0-9]{2,3}cm|hgt:[0-9]{2,3}in',
                    'hcl:#[0-9a-f]{6}',
                    'amb|blu|brn|gry|grn|hzl|oth',
                    'pid:[0-9]{9}']

subst_strings = ['byr:',
                 'iyr:', 
                 'eyr:',
                 'hgt:|cm|in',
                 'hcl:',
                 'ecl:',
                 'pid:']
count = 0


for passport in clean_data:
    validation = 0
    
    ##byr:
    if re.search(validation_regex[0],passport)!= None:
        dat = re.search(validation_regex[0],passport)
        dat = int(re.sub(subst_strings[0],"",dat[0]))
        if dat>=1920 and dat <= 2002:
            validation+=1
    ##iyr
    if re.search(validation_regex[1],passport)!= None:
        
        dat = re.search(validation_regex[1],passport)
        dat = int(re.sub(subst_strings[1],'',dat[0]))
        if dat>=2010 and dat <= 2020:
            validation+=1
    ##eyr
    if re.search(validation_regex[2],passport)!= None: 
        dat = re.search(validation_regex[2],passport)
        dat = int(re.sub(subst_strings[2],'',dat[0]))
        if dat>=2020 and dat <= 2030:
            validation+=1

    ##hgt
    if re.search(validation_regex[3],passport)!= None:
        dat = re.search(validation_regex[3],passport)
        if 'cm' in dat[0]:
            dat = int(re.sub(subst_strings[3],"",dat[0]))
            if dat >= 150 and dat <= 193:
                validation+=1
        elif 'in' in dat[0]:
            dat = int(re.sub(subst_strings[3],"",dat[0]))
            if dat >= 59 and dat <= 76:
                validation+=1
    ##hcl
    if re.search(validation_regex[4],passport)!= None:
        validation+=1
    
    ##ecl   
    if re.search(validation_regex[5],passport)!= None:
        
        validation+=1
    ##pid
    if re.search(validation_regex[6],passport)!= None:  
        validation+=1
    
    ##incrementing valid passport
    if validation == len(validation_regex):
        count+=1

print(count)