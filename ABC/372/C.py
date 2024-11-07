N, Q = map(int, input().split())
S = list(input())

for i in range(Q):
    x, c = input().split()
    x = int(x)

    S[x-1] = c
    print("".join(S).count("ABC"))