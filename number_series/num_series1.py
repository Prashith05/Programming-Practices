# Print the given series upto n numbers
# i/p: 10
# o/p: 2 1 4 3 6 5 8 7 10 9 
n = int(input("n: "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i-1,end=" ")
    else:
        print(i+1,end=" ")

# m= int(input("m: "))
# count = 2
# flag = 0
# while m != 0:
#     if flag == 0:
#         print(count,end=" ")
#         count -= 1
#     else:

