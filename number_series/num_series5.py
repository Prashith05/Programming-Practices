# i/p: n: 5
# o/p: 1 2 6 24 120 
n = int(input("n: "))
for i in range(1,n+1):
    s = 1
    while i != 0:
        s = s * i
        i -= 1
    print(s,end=" ")