import re
f = open('summery.txt')

data = f.read()
re.split('\s+', data)

print(data)
f.close()
