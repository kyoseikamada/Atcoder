Q = int(input())

S = {}

for i in range(Q):
    query = input()
    if len(query) > 1:
        q, x = map(int, query.split())
        if q == 1:
            if x in S:
                S[x] += 1
            else:
                S[x] = 1
        elif q == 2:
            S[x] -= 1
            if S[x] == 0:
                S.pop(x)
    else:
        x = int(query)
        print(len(S))