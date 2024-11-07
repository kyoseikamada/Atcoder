N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

for i in range(Q):
    b, k = map(int, input().split())

    tmp_A = [A[0] - b]
    ans = 0
    tmp_max = abs(A[0] - b)
    for j in range(1, N):
        d = abs(A[j] - b)
        if tmp_max >= d:
            tmp_A.append(d)
        else:
            if len(tmp_A) <= k:
                tmp_max = d
                tmp_A.append(d)
            else:
                break

    tmp_A_sorted = sorted(tmp_A)

    print(tmp_A_sorted[k-1])