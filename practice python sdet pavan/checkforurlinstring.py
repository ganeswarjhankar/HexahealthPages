"""Using Regular Expression """
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

#http://urlregex.com




import re
str="i m a great url for python https://www.tutorialsteacher.com/python/python-read-write-file"

str =" my profile : https://gooback.com,https://gooback.com,https://gooback.com,https://gooback.com,https://gooback.com"
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
print(url)
