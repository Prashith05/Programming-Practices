# PATTERN 1
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
print("---------- #P1 ----------")
print("Method #1")
n = int(input("n: "))
for i in range(1,n+1):
    print("* " *i)
for i in range(n-1,0,-1):
    print("* " *i)

print("Method #2")
n = int(input("n: "))
c = 0
for i in range(n):
    c += 1
    print("* " *(n-(n-c)))
for i in range(n):
    c -= 1
    print("* " *(n-(n-c)))

print("Method #3")
n = int(input("n: "))
for i in range(n-1,-n,-1):
    for j in range(n,abs(i),-1):
        print("*",end=" ")
    print()

print("---------------------------")

# PATTERN 2
#         *
#       * * *
#     * * * * * 
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
print("---------- #P2 ----------")
n = int(input("n: "))
b = n + 1
c = -1
for i in range ((n//2)+1):
    b -= 2
    c += 2
    print(" " *b + "* " *c)
for i in range ((n//2)+1):
    b += 2
    c -= 2
    print(" " *b + "* " *c)

print("---------------------------")

n = int(input("n: "))
b = n
c = 0
for i in range (n):
    b -= 1
    c += 1
    print(" " *b + "* " *c)
for i in range (n-1):
    b += 1
    c -= 1