# Question : Given a 2D list (matrix), write a program to transpose it.

A = [[1,2,3],
     [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]
for i in T:
    print(i)


    