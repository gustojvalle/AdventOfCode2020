from itertools import combinations
with open('./adventofcalendarinput2.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]


count = 0
for entry in data:
    policy,  password = entry.split(":")
    password = password.replace(" ","")
    pol_num , char = policy.split(" ")
    pol_num = pol_num.split("-")
    pol_num = [int(x) for x in pol_num]
    pol_num.sort()
    if (password.count(char) >= int(pol_num[0]) and password.count(char) < int(pol_num[1])+1):
        count+=1
print(count)