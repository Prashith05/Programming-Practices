# WAP to print the given series upto n values
# i/p: n: 5
# o/p: 1 4 7 10 13 
n = int(input("n: "))
count = 1
i = 1
while count <= n:
    print(i,end=" ")
    i += 3
    count += 1

print("\n-------------------------")
n = int(input("n: "))
x = 1
for i in range(1,n+1):
    print(x,end=" ")
    x = x + 3