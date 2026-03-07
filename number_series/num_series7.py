n= int(input("n: "))
for i in range(1,n+1):
    # print(f"i: {i}")
    p = 0
    s = 0
    while i != 0:
        r = i % 10
        # print(f"r: {r}")
        s = s + (2 ** p * r)
        i = i // 10
        p += 1
        # print(f"s: {s}")
        # print()
    print(s,end=" ")

# p = 0
# s = 0
# while n != 0:
#     r = n % 10
#     s = s + (2 ** p * r)
#     n = n // 10
#     p += 1
# print(f"Decimal Value --> {s}")

