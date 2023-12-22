lists = ["geeks", "geeks", "lucky"]
word = "geeks"

occur = 2

count = 0

for i in range(0, len(lists)-1):
        if (lists[i] == word):
            count = count + 1
            if (count == occur):
                del lists[i]

print(lists)


