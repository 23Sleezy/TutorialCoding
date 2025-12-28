# algorithm for bubble sorting
mylist = [8,5,4,3,7,6,9,11,123,1,120,99,88,223,213,2,0,15]
for i in range(0,len(mylist)):
    for j in range(0,len(mylist)-1): # -1 to compare adjacent value on the right
        first = mylist[j]
        second = mylist[j+1]
        if(first > second):
            temp_num = second
            mylist[j+1] = first
            mylist[j] = second
print(mylist)
mylist = [8,5,4,3,7,6,9,11,123,1,120,99,88,223,213,2,0,15]
for i in range(0, len(mylist)-1): # -1 to compare nearest value
#set min to index 0 (then find the minimum within the list)
    minimum = mylist[i]
    min_spot = i
    for j in range(i+1, len(mylist)):
        if(mylist[j] < minimum):
            min_spot = j # store minimum spot
            minimum = mylist[j]
    #now swap the new minimum with the selected spot
    temp = mylist[i]
    mylist[i] = minimum
    mylist[min_spot] = temp
print(mylist)