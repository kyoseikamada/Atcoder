
N = int(input())
A = []
TMP = []


for i in range(N):
    a = list(input())
    A.append(a)
    TMP.append(a.copy())


TMP_TMP = TMP.copy()


for i in range(N//2):
    for j in range(i, N-i):
        for k in range(j, N-i):
            A[k][N-1-j] = TMP[j][k]
            A[j][N-1-k] = TMP[k][j]
        
        TMP_TMP[j] = A[j].copy()
        TMP_TMP[k] = A[k].copy()
    TMP = TMP_TMP.copy()


for i in range(N):
    print("".join((A[i])))