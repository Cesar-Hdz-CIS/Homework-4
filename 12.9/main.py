# Cesar Hernandez
# 1835494

parts = input().split() #Split input into 2
name = parts[0] #set name from input
names = [] #empty name list
ages = [] #empty age list

while name !='-1' : #as long as input is not -1 continue the loop
    try:
        age = int(parts[1]) + 1
    except:
        age = 0
    names.append(name)
    ages.append(age)
    parts = input().split()
    name = parts[0]
for i in range(0,len(names)):
    print('{} {}'.format(names[i], ages[i]))