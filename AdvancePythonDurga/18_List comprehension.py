vowels=["a","e","i","o","u"]
word=(input(("Enter word which contain vowels")))
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)




