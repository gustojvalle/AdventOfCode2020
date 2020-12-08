import re

with open('./bags.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]



rules = {}
for line in data:
    vi = line.split("contain")
    vi[0] = vi[0].replace(" bags ", "")
    vi[1] = vi[1].split(",")
    if "no other bags" in line: 
        rules[vi[0]] = {"":""}
    else:
        intermediate={}
        for x in vi[1]:
            dict_entry = re.sub(r'bags|bag|\.| [0-9]', "", x)[1:len(re.sub(r'bags|bag|\.| [0-9]', "", x))-1]
            intermediate[dict_entry]=int(re.match(r' [0-9]+', x)[0])
        rules[vi[0]] = intermediate
            

def shiny_gold_checker(rule):
    keys = rules[rule].keys()
    if '' in keys:
        return False
    if "shiny gold" in keys or any(shiny_gold_checker(key) for key in keys):
        return True
    return False

    count = 0

for key in rules.keys():
    if shiny_gold_checker(key):
        count +=1
print("Solution for puzzle one: {}".format(count))

##solution puzzle 2##	
def digging_deep(bag, number):
	return number + sum(number*digging_deep(ent,num) for ent, num in rules[bag].items())

print("Soltion puzzle 2: {}".format(digging_deep("shiny gold", 1)-1))
