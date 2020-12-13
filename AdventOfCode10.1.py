from itertools import combinations
with open('./jolts.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [int(x.replace('\n',"")) for x in data]
data.append(max(data)+3)
sequence=[0]
data = sorted(data)
for i in  range(0, len(data)): 
	x = i
	entry = data[x]
	diffs=[]
	while (entry - sequence[-1])<4 and x <= len(data)-1: 
		entry = data[x]
		diffs.append(entry)
		x+=1
	sequence.append(min(diffs))

sequence= sorted(sequence)
diff =  [sequence[i]-sequence[i-1] for i in range(1, len(sequence))]
print("Answer is:  "+str((len([x  for x in diff if x ==1]))*(len([x  for x in diff if x ==3])))) 
