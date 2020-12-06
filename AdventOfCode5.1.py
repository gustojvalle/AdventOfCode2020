
#preparing data##
with open('./ticketinfo.txt') as file:
    my_input = file
    data=file.readlines()
    file.close()
    
data = [x.replace('\n',"") for x in data]




##solving the puzzle##
ids=[]
for line in data:
    row = line[:7]
    column  = line[-3:]
    rang_num = [0,127]
    rang_col= [0,7]
    for char in row:
        if char == 'F':
            rang_num = [rang_num[0],rang_num[0]+(rang_num[1]-rang_num[0])//2]
        elif char =='B':
            rang_num = [rang_num[0]+((rang_num[1]-rang_num[0])//2)+1,rang_num[1]]
        row_num = rang_num[0]
    
    
    for char in column:
        print(rang_col)
        if char == 'L':
            rang_col = [rang_col[0],rang_col[0]+(rang_col[1]-rang_col[0])//2]
        elif char =='R':
            rang_col = [rang_col[0]+((rang_col[1]-rang_col[0])//2)+1,rang_col[1]]
        col_num = rang_col[0]
    seat_id = row_num*8+col_num
    ids.append(seat_id)
    
print(max(ids))