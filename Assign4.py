print("Addition - ")
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[3,4,5],
   [1,4,7],
   [5,6,7]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
for r in result:
    print(r)

print("Substraction - ")
X=[[1,2,3],
   [4,5,6],
   [7,8,9]]
Y=[[3,4,5],
   [1,4,7],
   [5,6,7]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]-Y[i][j]
for r in result:
    print(r)

print("Multiplication - ")
C=[[1,2,3],
   [4,5,6],
   [7,8,9]]
D=[[3,4,5,3],
   [1,4,7,2],
   [5,6,7,5]]
result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(C)):
    for j in range(len(D[0])):
        for k in range(len(D)):
            result[i][j]+=C[i][k]*D[k][j]
for r in result:
    print(r)

print("Transpose - ")
S=[[1,2],
   [4,5],
   [7,8]]
result=[[0,0,0],
        [0,0,0]]
for i in range(len(S)):
    for j in range(len(S[0])):
        result[j][i]=S[i][j]
for r in result:
    print(r)
    
