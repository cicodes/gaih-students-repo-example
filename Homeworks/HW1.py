 #Create two lists
a = list(range(1,10,2))
b = list(range(0,10,2))

#Merge a,b lists
newList = a+b

#Multiple all values in the newList by 2 
newList = [i*2 for i in newList]

#Print the data type of all values in new list
for item in newList:
    print(type(item))
