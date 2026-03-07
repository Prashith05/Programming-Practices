# WAP to print PRIME NUMBERS upto the given range
# i/p: 5
# o/p: 2,3,5,7,11
n = int(input("n: "))
count = 0
num = 2
while count < n:
    flag = 0
    for i in range(1,num):
        if num % i == 0:
            flag += 1
    if flag == 1:
        print(num,end=" ")
        count +=1
    num += 1
    