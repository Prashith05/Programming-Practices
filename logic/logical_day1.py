# WAP to swap 2 numbers
# print("---------- #P1 ----------")
# x = int(input("x: "))
# y = int(input("y: "))
# print(f"\nBefore Swap\nx: {x}\t y: {y}")
# x,y = y,x
# print(f"\nAfter Swap\nx: {x}\t y: {y}")

# print("\n---------------------------")

# without any condition & without using any 0 find out if a num is odd or even
# print("---------- #P2 ----------\n")
# l = ["Even","Odd"]
# n = int(input("n: "))
# print(f"{n} is {l[n%2]}")

# print("\n---------------------------")


# To check if given num is ARMSTRONG NUMBER or not
# print("---------- #P3 ----------\n")
# n = int(input("n: "))
# temp = n
# s = 0
# while temp != 0:
#     r = temp % 10
#     s = s + (r ** len(str(n)))
#     temp = temp//10
# if n == s:
#     print(f"{n} is Armstrong")
# else:
#     print(f"{n} is not Armstrong")

# print("\n---------------------------")

# FACTORIAL
# print("---------- #P4 ----------\n")
# n = int(input("n: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"Factorial of {n} --> {fact}")

# print("\n---------------------------")

# a = 1
# while n > 0:
#     a = a * (n-1)

# WAP to check if a given number is a STRONG NUMBER or not(eg. 145, 40585)
# print("---------- #P5 ----------\n")
# n = int(input("n: "))
# temp = n
# s = 0
# while temp != 0:
#     r = temp % 10
#     fact = 1
#     for i in range(1,r+1):
#         fact = fact * i
#     s = s + fact
#     temp = temp//10
# if n == s:
#     print(f"{n} is Strong")
# else:
#     print(f"{n} is not Strong")

# print("\n---------------------------")

# WAP to find the sum digits of a given number
# print("---------- #P6 ----------\n")
# n = int(input("n: "))
# a = n
# s = 0
# while n > 0:
#     r = n % 10
#     s = s + r
#     n = n //10
# print(f"Sum of digits of {a} --> {s}")
# print("\n---------------------------")

# WAP to check if the given number is a perfect number or not(eg. 6, 28, 496, 8128)
# 6 is a perfect num..its factors(except the number itself) -> 1,2,3..... 1+2+3 = 6
# print("---------- #P7 ----------\n")
# n =int(input("n: "))
# s = 0
# for i in range(1,n):
#     if n % i == 0:
#         s = s + i
# if n == s:
#     print(f"{n} --> Perfect number")
# else:
#     print(f"{n} --> Not a Perfect number")
# print("\n---------------------------")

# WAP to reverse the given number and check whether it is a palindrome number or not
# print("---------- #P8 ----------\n")
# n = int(input("n: "))
# temp = n
# s = 0
# while temp != 0:
#     r = temp % 10
#     s = s * 10 + r
#     temp = temp // 10
# if s == n:
#     print(f"{n} --> Palindrome")
# else:
#     print(f"{n} --> Not Palindrome")
# print("\n---------------------------")

# WAP to display frequency of each number from the given number
# i/p: 1237793 
# o/p: 1 --> 1 , 2 --> 1 , 3 --> 2 , 7 --> 2 , 9 --> 1
# print("---------- #P9 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# for i in range(1,10):
#     count = 0
#     temp = n
#     while temp != 0:
#         r = temp % 10
#         if r == i:
#             count += 1
#         temp = temp // 10
#     if count != 0:
#         print(f"{i} --> {count}")

# print("\nMethod 2")
# n =int(input("n: "))
# d = {}
# temp = n
# while temp != 0:
#     r = temp % 10
#     if r not in d:
#         d[r] = 1
#     else:
#         d[r] += 1
#     temp = temp // 10
# for i,j in d.items():
#     print(f"{i} --> {j}")

# print("\n---------------------------")

# WAP to check the given number is a DISARIUM number or not
# print("---------- #P10 ----------\n")
# n = int(input("n: "))
# val = n
# # l = len(str(n))
# count = 0
# while val != 0:     # getting the length of a number without len() 
#     count += 1
#     val = val // 10
# temp = n
# s = 0
# while temp != 0:
#     r = temp % 10
#     s = s + r ** count
#     count -= 1
#     temp = temp // 10
# if s == n:
#     print(f"{n} --> Disarium Number")
# else:
#     print(f"{n} --> Not Disarium Number")
# print("\n---------------------------")

# WAP to find SUPER DIGIT of a given number
# add the digits of a num and get the sum...if sum less than 10 then it is the super digit..else again add
# the sum till u get a single digit number
# i/p: 86143254     o/p: 6
# print("---------- #P11 ----------\n")
# n = int(input("n: "))
# temp = n
# while n > 10:    
#     s = 0
#     while n != 0:
#         r = n % 10
#         s = s + r
#         n = n // 10
#     n = s
# print(f"Super digit of {temp} --> {s}")

# print("\n---------------------------")

# WAP to check the given number is an AUTOMORPHIC NUMBER is not 
# print("---------- #P12 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# l = 10
# temp = n
# sq = n * n
# flag = False
# while n != 0:
#     r = sq % l
#     if r == temp:
#         flag = True
#     l = l * 10
#     n = n // 10
# if flag == True:
#     print(f"{temp} --> Automorphic number")
# else:
#     print(f"{temp} --> Not Automorphic number")
# print("\n---------------------------")

# print("Method 2")
# n = int(input("n: "))
# l = len(str(n))
# sq = n * n
# temp = n
# s = 0
# while temp != 0:
#     r = temp % 10
#     s = s * 10 + r
#     temp = temp // 10
# s1 = 0
# while s != 0:
#     r = s % 10
#     s1 = s1 * 10 + r
#     s = s // 10
# if s1 == n:
#     print(f"{n} --> Automorphic number")
# else:
#     print(f"{n} --> Not Automorphic number")


# WAP to check the given number is a MIRROR NUMBER or not
# print("---------- #P13 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# temp = n
# count = 0
# while temp != 0:
#     count += 1
#     temp = temp // 10
# s1 = 0
# s2 = 0
# if count % 2 == 0:
#     temp = n
#     count = count // 2
#     a = temp // 10 ** count
#     while a != 0:
#         r1 = a % 10
#         s1 = s1 + r1
#         a = a// 10
#     temp = n
#     while count != 0:
#         r2 = temp % 10
#         s2 = s2 + r2
#         temp = temp // 10
#         count -= 1
#     if s1 == s2:
#         print(f"{n} --> Mirror number")
#     else:
#         print(f"{n} --> Not Mirror number")
# else:
#     print(f"{n} --> Not Mirror number")

# print("\nMethod 2")
# n = int(input("n: "))
# temp = n
# count = 0
# while temp != 0:
#     count += 1
#     temp = temp // 10
# s1 = 0
# s2 = 0
# if count % 2 == 0:
#     temp = n
#     count = count // 2
#     a = temp // 10 ** count
#     b = temp % 10 ** count
#     while count != 0:
#         r1 = a % 10
#         r2 = b % 10 
#         s1 = s1 + r1
#         s2 = s2 + r2
#         a = a // 10
#         b = b // 10
#         count -= 1
#     if s1 == s2:
#         print(f"{n} --> Mirror number")
#     else:
#         print(f"{n} --> Not Mirror number")
# else:
#     print(f"{n} --> Not Mirror number")


# print("\n---------------------------")


# -------------------------------------------
# n = 1221
# cnt = 0
# temp = n
# while n != 0:
#     cnt += 1
#     n = n//10
# print(cnt)
# if cnt%2==0:
#     print(temp%10**(cnt//2))


# WAP to display the maximum number frm the given number
# print("---------- #P14 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# flag = 0
# for i in range(9,0,-1):
#     temp = n
#     while temp != 0:
#         r = temp % 10
#         if r == i:
#             flag = 1
#             break
#         temp = temp // 10
#     if flag == 1:
#             break
# print(f"Maximum element --> {i}")

# print("\nMethod 2")
# n = int(input("n: "))
# max_ele = 0
# while n != 0:
#     r = n % 10
#     if r > max_ele:
#         max_ele = r
#     n = n // 10
# print(f"Maximum element --> {max_ele}")

# print("\n---------------------------")

# Print 1st two maximum elements frm the given number and display its difference
# print("---------- #P15 ----------\n")
# n = int(input("n: "))
# temp = n
# max_ele_1 = 0
# max_ele_2 = 0
# while n != 0:
#     r = n % 10
#     if r > max_ele_1:
#         max_ele_1 = r
#     n = n // 10
# while temp != 0:
#     r = temp % 10
#     if r > max_ele_2:
#         if r != max_ele_1:
#             max_ele_2 = r
#     temp = temp // 10
# if max_ele_2 == 0:
#     print("There is no 2nd maximum number, so can't find difference") 
# else:
#     print(f"Maximum element 1 --> {max_ele_1}")
#     print(f"Maximum element 2 --> {max_ele_2}")
#     print(f"Difference --> {max_ele_1 - max_ele_2}")
# print("\n---------------------------")

# WAP to check given number is a FASINATING NUMBER or not (eg, 192, 273)
# print("---------- #P16 ----------\n")
# n = int(input("n: "))
# n1 = n * 1
# n2 = n * 2
# n3 = n * 3
# l = [0]*10
# while n1 != 0:
#     r = n1 % 10
#     l[r] += 1
#     n1 = n1 // 10
# while n2 != 0:
#     r = n2 % 10
#     l[r] += 1
#     n2 = n2 // 10
# while n3 != 0:
#     r = n3 % 10
#     l[r] += 1
#     n3 = n3 // 10
# for i in range(1,10):
#     if l[i] != 1:
#         print("Not a Fascinating Number")
#         break
#     # else:
#     #     print("Fascinating Number")
#     #     break
# else:
#     print("Fascinating Number")
# print("\n---------------------------")

# WAP to check if a given number is PRIME or not
# print("---------- #P17 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# count = 0
# if n <= 0:
#     print("Enter a number greater than 1")
# else:
#     if n == 1:
#         print(f"{n} --> Neither Prime nor Composite")
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 count += 1
#         if count == 0:
#             print(f"{n} --> Prime Number")
#         else:
#             print(f"{n} --> Not Prime Number")


# print("\nMethod 2")
# n = int(input("n: "))
# if n <= 0:
#     print("Enter a number greater than 1")
# else:
#     if n == 1:
#         print(f"{n} --> Neither Prime nor Composite")
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 print(f"{n} --> Not Prime Number")
#                 break
#             print(f"{n} --> Prime Number")
# print("\n---------------------------")

# WAP to convert a given number into its binary format
# print("---------- #P18 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# temp = 1
# b = 0
# while n != 0:
#     r = n % 2
#     b = b + temp * r
#     temp = temp * 10
#     n = n // 2
# print(b)

# print("\nMethod 2")
# n = int(input("n: "))
# temp = n
# s = 0
# while temp != 0:
#     a = temp % 2
#     print(f"a: {a}")
#     s = a * 10 + s
#     print(f"s: {s}")
#     temp = temp // 2
#     print(f"temp : {temp}")
# print(s)
# print("\n---------------------------")

# WAP to check the given number is EVIL NUMBER or not
# the number whose binary value have even no of 1's
# print("---------- #P19 ----------\n")
# print("Method 1")
# n = int(input("n: "))
# temp = 1
# b = 0
# count = 0 
# while n != 0:
#     r = n % 2
#     if r == 1:
#         count += 1
#     n = n // 2
# if count % 2 == 0:
#     print("Evil Number")
# else:
#     print("Not Evil Number")

# print("\nMethod 2")
# n = int(input("n: "))
# temp = 1
# b = 0
# while n != 0:
#     r = n % 2
#     b = b + temp * r
#     temp = temp * 10
#     n = n // 2
# count = 0
# while b != 0:
#     r = b % 10
#     if r == 1:
#         count += 1
#     b = b // 10
# if count % 2 == 0:
#     print("Evil Number")
# else:
#     print("Not Evil Number")

# print("\n---------------------------")

# WAP to convert given binary value to its decimal
print("---------- #P20 ----------\n")
n = int(input("n: "))
p = 0
s = 0
while n != 0:
    r = n % 10
    s = s + (2 ** p * r)
    n = n // 10
    p += 1
print(f"Decimal Value --> {s}")
print("\n---------------------------")


# print("---------- #P21 ----------\n")

# print("\n---------------------------")


# print("---------- #P22 ----------\n")
# print("\n---------------------------")


# print("---------- #P23 ----------\n")
# print("\n---------------------------")