# 0 1 1 2 3 5 8 13
# fibanocci
n = int(input("n: "))
a,b = 0,1
if n <= 0:
    print("Enter value greater than 0")
else:
    for i in range(n):
        print(a,end=" ")
        c = a + b
        a,b = b,c

print()

# error
# n = int(input("n: "))
# l =[]
# a,b = 0,1
# if n <= 0:
#     print("Enter value greater than 0")
# else:
#     if n == 1:
#         l=[0]
#     elif l == 2:
#         l = [0,1]
#     else:
#     for i in range(n-2):
#         c = a + b
#         a,b = b,c
#         l.append(c)
#     print(l)