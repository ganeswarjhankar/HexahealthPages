#Formal Arguments



"""Positional Arguments
Keyword argument
Default Arguments
variable Arguments"""





def sum(*n):
    total=0
    for i in n:
        total=total+i
        print("the sum ",total)
sum()
sum(10)
sum(10,20,30,40)

