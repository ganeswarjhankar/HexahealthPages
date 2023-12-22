# max() and
# split and range


numbers = input("Enter the list of numbers")
numbers_list = numbers.split()
# to set the limit of range function below for loop is used
count = 0
for i in numbers_list:
    count = count + 1

# to convert the string to integer in the list
for i in range(0, count):
    numbers_list[i] = int(numbers_list[i])

print(numbers_list)

# 34 45 12 3
maximum_number = numbers_list[0]  # 34
for number in numbers_list:
    if number > maximum_number:
        maximum_number = number

min_number = numbers_list[0] #34
for number in numbers_list:
    if number < min_number:
        min_number = number

print(maximum_number)
print(min_number)



