N = int(input())

L = []
R = []
LR = {}

for i in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    LR[i] = (l,r)

ans = [0]*N

if not (sum(L) <= 0 and sum(R) >= 0):
    print("No")
else:
    LR_sorted = sorted(LR.items(), key=lambda x:x[1][0], reverse=True)
    sum_x = LR_sorted[0][1][0]
    ans[LR_sorted[0][0]] = LR_sorted[0][1][0]
    for i in range(1, N):
        l = LR_sorted[i][1][0]
        r = LR_sorted[i][1][1]

        if sum_x != 0 and sum_x > 0 and sum_x + l > 0:
            ans[LR_sorted[i][0]] = l
            sum_x += l
        else:
            ans[LR_sorted[i][0]] = -sum_x
            sum_x = 0

    print("Yes")
    print(*ans)