mylist=["lucky","20","lucky"]
word="lucky"
n=2
count=0
for i in range(0,len(mylist)):
    if (mylist[i]==word):
        count=count+1
        if count==n:
            del mylist[i]

print(mylist)

