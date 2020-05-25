import numpy as np
def LUdecomposition(a, n):
    lower = [[0 for x in range(n)]  
            for y in range(n)]
    upper = [[0 for x in range(n)]  
            for y in range(n)]
    
    for i in range(n) :
    
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
            
            upper[i][k] = a[i][k] - sum
    
        for k in range(i, n):
            if(i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = (a[k][i] - sum)/(upper[i][i])
        
    upper = np.array(upper)
    lower = np.array(lower)
    print("U:\n", upper)
    print("L:\n", lower)

n = int(input("Enter a size of matrix:\n"))
a = np.zeros((n, n))
for i in range(n):
    row = []
    row = list(map(int, input("Enter a " + str(i) + " row of matrix: ").strip().split()))
    for j, val in zip(range(n), row):
        a[i][j] = val
print("Matrix is:\n", a)
LUdecomposition(a, n)