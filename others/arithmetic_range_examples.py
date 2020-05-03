'''generating arithmetic examples '''

add = 1
count = 1
total = ''
eight = '8'
for i in range(1, 13):
    #total = int(eight) + i 
    while add <= i:
        #print(add, end=' ')
        
        #add+=1
        total =add * int(eight) + i 
        print(add,'*', eight, '+', i,'=', total)
        count+=1
        add+=1
