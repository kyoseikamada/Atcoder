N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for i in range(N):
    if i == K-1:
        ans.append(A[i])
        ans.append(X)
    else:
        ans.append(A[i])

print(*ans)
        