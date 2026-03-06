#to just print a star
print("#P1")
print("*")
print()

# to print 2 start(each in 1 row)
print("#P2")
print("*")
print("*")
print()

#pattern to print 3 stars(one in each row)
# Controlling the no.of rows
print("#P3")
for i in range(3):
    print("*")

print()

#frm user input
print("#P4")
row = int(input("row: "))
for i in range(row):
    print("*")

print()

#STEPS:
# 1. Control the no.of rows (with a for loop)
# 2. Control the no.of columns (inside the 1st loop using a 2nd for loop)

# need 4 rows but 2 columns
print("#P5")
row = int(input("row: "))
for i in range(row):
    print("* *")

print()

# to print row * column matrix
# take row and column count frm user
print("#P6")
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()

print()

# to print:(if row = 3, col = 3)
#   1 2 3 
#   4 5 6
#   7 8 9
print("#P7")
count = 1
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print(count,end=" ")
        count += 1
    print()

print()

# row = int(input("row: "))
# col = int(input("col: "))
# for k in range(1,11,1):
#     for i in range(row):
#         for j in range(col):
#             print(k,end=" ")
#         print()

# to make a perfect matrix
#    01 02 03 04 
#    05 06 07 08
#    09 10 11 12
#    13 14 15 16
print("#P8")
count = 1
row = int(input("row: "))
col = int(input("col: "))
l = len(str(row*col))   # checking the length of the last number in the matrix so as to check how many zeors to put
for i in range(row):
    for j in range(col):
        print(str(count).zfill(l),end=" ")
        count += 1
    print()

print()

# To print: (row: 4, col: 4)
#    1 1 1 1 
#    2 2 2 2
#    3 3 3 3
#    4 4 4 4
print("#P9")
count = 1
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print(count,end=" ")
    count += 1
    print()

print()

# ALTERNATE METHOD:
print("#P10")
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print(i+1,end=" ")
    print()

print()

# if the row is greater than 9, then start frm 1
# To print: (row:10, col:3 )
#    1 1 1
#    2 2 2
#    3 3 3
#    4 4 4
#    5 5 5
#    6 6 6
#    7 7 7
#    8 8 8
#    9 9 9
#    1 1 1
print("#P11")
count = 1
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print(count,end=" ")
    count += 1
    print()
    if count > 9:
        count = 1

print()

# To print: (row:4, col:4)
#     1 2 3 4 
#     1 2 3 4 
#     1 2 3 4 
#     1 2 3 4
print("#P12")
count = 1
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    for j in range(col):
        print(count,end=" ")
        count += 1
    print()
    count = 1

print()

print("#P13")
# To print(row:3, col:4)
#   3 3 3 3
#   2 2 2 2
#   1 1 1 1
row = int(input("row: "))
col = int(input("col: "))
count = row
for i in range(row):
    for j in range(col):
        print(count,end=" ")
    print()
    count -=1

print()

# if the row is greater than 9, then start frm 9 and after reaching 1,again start from 9
# else start with the row itself
# To print: (row: 11, col: 4)
#     9 9 9 9 
#     8 8 8 8
#     7 7 7 7
#     6 6 6 6
#     5 5 5 5
#     4 4 4 4
#     3 3 3 3
#     2 2 2 2
#     1 1 1 1
#     9 9 9 9
#     8 8 8 8
print("#P14")
row = int(input("row: "))
col = int(input("col: "))
count = row
if count > 9:
    count = 9
for i in range(row):
    for j in range(col):
        print(count,end=" ")
    print()
    count -= 1
    if count == 0:
        count = 9

print()

# To print: (row:4, col:5)
#     5 4 3 2 1 
#     5 4 3 2 1
#     5 4 3 2 1
#     5 4 3 2 1
print("#P15")
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    count = col
    for j in range(col):
        print(count,end=" ")
        count -= 1
    print()

print()

# To print: (row: 4, col:5)
#     A A A A A 
#     B B B B B   
#     C C C C C
#     D D D D D
print("#P16")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    val += 1
    print()

print()

# To print: (row:4, col:3)
#     A A A 
#     B B B
#     C C C
#     D D D
print("#P17")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    val += 1
    print()

print()

# To print: (row:4, col:5)
#     A B C D E 
#     A B C D E 
#     A B C D E 
#     A B C D E 
print("#P18")
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    val = ord('A')
    for j in range(col):
        print(chr(val),end=" ")
        val += 1
    print()

print()

# if the char exceeds 'Z' then set it back to 'A' and then continue
# To print(row:30, col:9)
#    A A A A A A A A A  
#    B B B B B B B B B 
#    C C C C C C C C C 
#    D D D D D D D D D 
#    E E E E E E E E E 
#    F F F F F F F F F 
#    G G G G G G G G G 
#    H H H H H H H H H 
#    I I I I I I I I I 
#    J J J J J J J J J 
#    K K K K K K K K K 
#    L L L L L L L L L 
#    M M M M M M M M M 
#    N N N N N N N N N 
#    O O O O O O O O O 
#    P P P P P P P P P 
#    Q Q Q Q Q Q Q Q Q 
#    R R R R R R R R R 
#    S S S S S S S S S 
#    T T T T T T T T T 
#    U U U U U U U U U 
#    V V V V V V V V V 
#    W W W W W W W W W 
#    X X X X X X X X X 
#    Y Y Y Y Y Y Y Y Y 
#    A A A A A A A A A 
#    B B B B B B B B B 
#    C C C C C C C C C 
#    D D D D D D D D D 
#    E E E E E E E E E 
print("#P19")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    val += 1
    print()
    if val == ord('Z'):
        val = ord('A')

print()

# To print: (row:5, col:4)
#   E E E E 
#   D D D D 
#   C C C C 
#   B B B B 
#   A A A A 
print("#P20")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A') + row - 1
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    val -= 1
    print()

print()

# to print(row:5, col:4)
#    D C B A 
#    D C B A 
#    D C B A 
#    D C B A
#    D C B A
print("#P21")
row = int(input("row: "))
col = int(input("col: "))
for i in range(row):
    val = ord('A') + col - 1
    for j in range(col):
        print(chr(val),end=" ")
        val -= 1
    print()

print()

# To print(row:4, col:3)
#    A B C 
#    D E F
#    G H I
#    J K L
print("#P22")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
        val += 1
    print()

print()

# if the char becomes 'Z', then start frm 'A' again
# To print(row:5, col:6)
#    A B C D E F 
#    G H I J K L 
#    M N O P Q R 
#    S T U V W X 
#    Y Z A B C D 
print("#P23")
row = int(input("row: "))
col = int(input("col: "))
val = ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
        val += 1
        if val > ord('Z'):
            val=ord('A')
    print()

print()

# ASSIGNMENT 1
# To print(row:4, col:4)
#     Z Y X W 
#     V U T S 
#     R Q P O 
#     N M L K 
row = int(input("row: "))
col = int(input("col: "))
val = ord('Z')
for i in range(row):
    for j in range(col):
        print(chr(val),end=" ")
    val -= 1
    print()



#     Z Z Z Z 
#     Y Y Y Y 
#     X X X X
#     W W W W 

#     Z Y X W 
#     Z Y X W 
#     Z Y X W 
#     Z Y X W 

# 5 4
#     1 1 1 1
#     A A A A 
#     2 2 2 2
#     B B B B 
#     3 3 3 3

# 4 5

#     1 A 2 B 3
#     1 A 2 B 3
#     1 A 2 B 3
#     1 A 2 B 3

# 4 4 
#     1 A 2 B 
#     3 C 4 D 
#     5 E 6 F 
#     7 G 8 H 

# 5 5 
#     1 A 2 B 3 
#     C 4 D 5 E 
#     6 F 7 G 8 
#     H 9 I 10 J 
#     11 K 12 L 13

