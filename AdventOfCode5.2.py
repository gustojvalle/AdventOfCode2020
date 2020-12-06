
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
    
##calculate all the possible ticket_ids##
all_tickets = []
for i in range(127):
    row_id = i*8
    for i in range(7):
        ticket_id = row_id+i
        all_tickets.append(ticket_id)
main_list = list(set(all_tickets)-set(ids))
print(main_list)