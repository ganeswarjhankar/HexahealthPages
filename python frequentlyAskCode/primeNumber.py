n=int(input("enter the number"))
flag=0
if n>1:
    for i in range(1, n + 1):
        if (n % i) == 0:
            flag = flag + 1

    if flag == 2:
        print("Prime Numebr")
    else:
        print("Non prime")


