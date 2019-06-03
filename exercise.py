
num = range(1,51)
dict = {}

for n in num:
    if n%2 == 0 and n%7 == 0:
        dict[n] = n*2
    elif n%2 == 0: 
        dict[n] = n+1
    elif n%7 == 0: 
        dict[n] = n-1
    else:
        dict[n] = n

print(dict)