##Sorting the Data out##
from itertools import combinations
with open('./adventofcalendarinput2.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()

data = [x.replace('\n',"") for x in data]


###Solving the Puzzle ###
count = 0
for entry in data:
    policy,  password = entry.split(":")
    password = password.replace(" ","")
    pol_num , char = policy.split(" ")
    pol_num = pol_num.split("-")
	    if ((password[int(pol_num[0])-1] == char and password[int(pol_num[1])-1] != char) or 
       (password[int(pol_num[0])-1] != char and password[int(pol_num[1])-1] == char)):
        count+=1
print(count)