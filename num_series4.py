# i/p: n: 5
# o/p: 1 8 9 64 25 
n = int(input("n: "))
for i in range(1,n+1):
    if i % 2 == 1:
        print(i**2,end=" ")
    else:
        print(i**3,end=" ")