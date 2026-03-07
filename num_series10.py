# i/p: 1
# o/p: 1 * a

# i/p: 3
# o/p: 1 * a 2 * b 3 * c

print("Method 1")
n = int(input("n: "))
val1 = 1
val2 = ord('a')
for i in range(n):
    if val1 == 27:
         val2 = ord('a')
    print(f"{val1} * {chr(val2)}",end=" ")
    val1 += 1
    val2 += 1

print()

print("\nMethod 2")
n = int(input("n: "))
m = 1
star = "*"
char = 97
for i in range(n):
    print(m,end=" ")
    m += 1
    print(star,end=" ")
    if char <= 122:
        print(chr(char),end=" ")
        char += 1
    else:
        char = 97