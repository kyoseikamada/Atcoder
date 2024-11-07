N, K = map(int, input().split())

A = {}
B = {}

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b


oneday_sum = sum(list(B.values()))

if oneday_sum <= K:
    print(1)
else:
    sabun = oneday_sum - K
    A_sorted = sorted(A.items(), key=lambda x:x[1])

    nanichi = 0
    goukei = 0
    for i in range(N):
        a_sorted = A_sorted[i]
        day = a_sorted[1]
        index = a_sorted[0]

        goukei += B[index]
        if goukei >= sabun:
            nanichi = day + 1
            break
        else:
            nanichi = day
            continue

    
    print(nanichi)