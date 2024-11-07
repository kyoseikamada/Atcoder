N, M = map(int, input().split())

M = []

for i in range(N):
    M.append(list(map(int, input().split())))


ans = False

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            P_i = M[i][0]
            C_i = M[i][1]
            F_i = set(M[i][2:C_i+1])
            P_j = M[j][0]
            C_j = M[j][1]
            F_j = set(M[j][2:C_j+1])

            if P_i >= P_j and F_j >= F_i and (P_i > P_j or F_j > F_i):
                ans = True
                break


if ans:
    print("Yes")
else:
    print("No")