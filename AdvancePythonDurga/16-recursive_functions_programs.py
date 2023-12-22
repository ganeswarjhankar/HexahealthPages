def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

object=factorial(3)
print(object)






