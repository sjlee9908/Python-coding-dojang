import re

url=input()
if re.match('^http[s]*\:\/\/[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.&?=]*', url):
    print(True)
else:
    print(False)