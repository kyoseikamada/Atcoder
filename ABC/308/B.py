N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))
         
Price = 0

for c in range(N):
    if C[c] not in set(D):
        Price += P[0]
    else:
        for d in range(M):
            if C[c] == D[d]:
                Price += P[d+1]
                break


print(Price)
    