# find the average of each height of person in the given list


#153 133 343 55 333 556


heights = input("enter all the heights separated by space:")

heights_list1 = heights.split()
count = 0
for height in heights_list1:
    count = count + 1
print(count)
for i in range(0, count):
    heights_list1[i] = int(heights_list1[i])

print((heights_list1))

total = 0
for y in heights_list1:
    total = y + total

print(total)

avg1 = total / count
print(round(avg1))





