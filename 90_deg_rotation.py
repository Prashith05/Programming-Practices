'''
    WAP to rotate the given matrix to 90 deg to right side and display the output make sure that no.of columns 
    should be same

1 2 3       7 4 1
4 5 6       8 5 2
7 8 9       9 6 3


00 01 02
10 11 12
20 21 22

'''

row = int(input("rows: "))
col = int(input("col: "))
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("----- MATRIX  -----")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

print("----- ROTATED MATRIX  -----")
for i in range(row):
    for j in range(col-1,-1,-1):
        print(matrix1[j][i],end=" ")
    print()

result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[j][i]
for i in range(len(result)):
    result[i] = result[i][::-1]
print("----- ROTATED MATRIX  -----")
for i in range(row):
    for j in range(col):
        print(result[i][j],end=" ")
    print()