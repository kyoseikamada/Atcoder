N, K = map(int, input().split())
P = list(map(int, input().split()))
P_tmp = P.copy()

for k in range(K):
    for i in range(N):
        pi = P[i]-1
        P_pi = P[pi]
        P_tmp[i] = P_pi
    P = P_tmp.copy()

print(*P)