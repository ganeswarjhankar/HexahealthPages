import re

str="dsfsd!@$#%^&*()(&^^%%dsdsfdfd"
regex=re.compile('[!@#$%^&*()_+~]')

if (regex.search(str))==None:
    print("No special character present in string")
else:
    print("String contains spl characters")





