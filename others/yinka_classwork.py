#make difference strings of seven words, including one figure.
#Concatenate them inside a list, and print out the list


the_list = [5, 'london', 'bridges', 'are', 'falling', 'down','right', 'now']

#print(the_list)
print()


m = 'Monday'
t = 'Tuesday'
w = 'Wednesday'
t2 = 'Thursday'
f = 'Friday'
s = 'Saturday'
s2 = 'Sunday'

week_days = [m,t,w,t2,f,s,s2]
'''m = week_days[0] + ' ' + week_days[1]  
#print(m)'''

#print(week_days)

'''new_weeks = ' '
for i in week_days:
    if i != "'" and i != ' ':
        new_weeks += i
        print(i, end=' ')


i = 0
while i < 7:
    j = week_days[i] + ' '
    print(j, end= ' ')
    i += 1

myList = [1, 'a', 3.14159, True]

print(myList[1])
print(myList[:3])'''


def are_anagram(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    print(word1_sorted, word2_sorted)

    if word1_sorted == word2_sorted:
        return True
    else:
        return False

