from collections import deque

N = int(input())
S = input()

Q = deque()

ans = ""

KOHO = ""

for i in range(N):
    if S[i] == "(" and len(KOHO) > 0:
        Q.append(KOHO)
        KOHO = S[i]
    elif S[i] == "(" and len(KOHO) == 0:
        KOHO += S[i]
    elif S[i] != "(" and S[i] != ")" and len(KOHO) > 0:
        KOHO += S[i]
    elif S[i] != "(" and S[i] != ")" and len(KOHO) == 0:
        if len(Q) > 0:
            KOHO = Q.pop() + S[i]
        else:
            ans += S[i]
    elif S[i] == ")" and len(KOHO) > 0:
        KOHO = ""
    elif S[i] == ")" and len(KOHO) == 0:
        if len(Q) > 0:
            Q.pop()
        else:
            ans += S[i]
    


if KOHO != "":
    Q.append(KOHO)

Q_len = len(Q)

for i in range(Q_len):
    ans += Q.popleft()


print(ans)