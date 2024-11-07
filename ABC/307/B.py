N = int(input())

S = []

for i in range(N):
    S.append(input())


ans = False

for i in range(N):
    for j in range(N):
        if i == j:
            next
        else:
            S_ij = S[i] + S[j]
            is_kaibun = True
            for k in range(len(S_ij)):
                if S_ij[k] == S_ij[len(S_ij)-1-k]:
                    continue
                else:
                    is_kaibun = False
            if is_kaibun:
                ans = True

if ans:
    print("Yes")
else:
    print("No")