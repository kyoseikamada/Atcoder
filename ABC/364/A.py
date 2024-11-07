N = int(input())
S = []

for i in range(N):
    S.append(input())

ans = True

for i in range(N-1):
    if S[i] == "sweet" and S[i+1] == S[i] and i != N-2:
        ans = False
    else:
        next

if ans:
    print("Yes")
else:
    print("No")