mylist=[1,2,3,4,5,5,5,6,6,7,7]
x=5
count=0
for element in mylist:
    if element==x:
        count=count+1

print(count)
print(x)
print("{} Occurence number {}:".format(x,count))



