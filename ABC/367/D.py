N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    count = 0
    for j in range(i+1, N+i):
        if j >= N:
            j = j % N
            count += A[j-1]
            if count % M == 0:
                ans += 1
        else:
            count += A[j-1]
            if count % M == 0:
                ans += 1

print(ans)