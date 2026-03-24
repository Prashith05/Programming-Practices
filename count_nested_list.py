# WAP to count the no.of list present inside a list and find the sum of only integer values

l = ['A',33.6,74,[7],4,'a',[3,'$',4],[3,'a',11],17,[12,4]]
count = 0
sum = 0
for i in l:
    if isinstance(i,list):
        count += 1
        for j in i:
            if isinstance(j,int):
                sum += j
    if isinstance(i,int):
        sum += i 
print(f"count: {count}")
print(f"sum: {sum}")