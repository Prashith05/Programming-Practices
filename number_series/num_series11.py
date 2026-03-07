# i/p: 5
# o/p: 1 2 3 4 5

# i/p: 33
# o/p: 1 2 3 4 5 * * * * * A B C D E 1 2 3 4 5 * * * * * A B C D E 1 2 3
n = int(input("n: "))
l = [1,2,3,4,5,"*","*","*","*","*","A","B","C","D","E"]
l1 = []
l2 = []
if n >= 16:
    k = n // 15
    m = n % 15
    l2 = k * l
    for j in range(m):
        l1.append(l[j])
    l2.extend(l1)
    for i in range(n):
        print(l2[i],end=" ")
else:
    for i in range(n):
        print(l[i],end=" ")


