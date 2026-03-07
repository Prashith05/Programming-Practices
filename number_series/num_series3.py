# i/p: n: 5
# o/p: 5 10 20 40 80 
n = int(input("n: "))
count = 1
i = 5
while count <= n:
    print(i,end=" ")
    i = i * 2
    count += 1

print("\n-------------------------")

n = int(input("n: "))
x = 5
for i in range(1,n+1):
    print(x,end=" ")
    x = x * 2