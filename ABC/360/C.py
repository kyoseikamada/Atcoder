N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

hako = [[] for i in range(N)]
hako_isnotnull = [False]*N

for i in range(N):
    hako[A[i]-1].append(W[i])
    hako_isnotnull[A[i]-1] = True


ans = 0

for i, h in enumerate(hako):
    if hako_isnotnull[i] and len(h) > 1:
        h_t = sorted(h)
        ans += sum(h_t[:len(h_t)-1])

print(ans)
