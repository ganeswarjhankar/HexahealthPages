#using set value to find common


def common_value():
    list1 = input("enter the value: ")
    list2 = input("enter the value: ")
    s1 = set(list1)
    s2 = set(list2)
    print(s1)
    print(s2)

    lst = s1 & s2
    print(lst)


common_value()

























