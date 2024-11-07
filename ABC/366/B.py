N = int(input())
S = []
max_S = 0

for i in range(N):
    s = input()
    S.append(s)
    if max_S < len(s):
        max_S = len(s)

ans = [["*"]*N for i in range(max_S)]

for i in range(N):
    s = S[i]
    for j in range(len(s)):
        ans[j][(N-1) - i] = s[j]

for i in range(max_S):
    s = ans[i]
    if s[len(s)-1] == "*":
        ans[i][len(s)-1] = ""
        for j in range(len(s) - 2, 0, -1):
            if s[j] == "*":
                ans[i][j] = ""
            else:
                break


for i in range(len(ans)):
    print("".join(ans[i]))