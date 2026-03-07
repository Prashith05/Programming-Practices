# i/p: pyspiders , n = 12
# o/p: p Y s P i D e R s P y S

# s ="pyspiders"
s = input("s: ")
n = int(input("n: "))
flag = 0
count = 0
for i in range(n):
    if flag == 0:
        print(s[count].lower(),end=" ")
        flag = 1
        count += 1
    else:
        print(s[count].upper(),end=" ")
        flag = 0
        count += 1
    if count == len(s):
        count = 0