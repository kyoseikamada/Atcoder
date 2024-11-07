H, W, K = map(int, input().split())

S = []

T = [[[]]* W for _ in range(H)]

for i in range(H):
    s = list(input())
    S.append(s)


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if i + 1 < H:
                if S[i+1][j] == ".":
                    T[i+1][j].append(S[i][j].append((i,j)))

            if i - 1 > -1:

            
            if j + 1 < W:
            

            if j -1 > -1:

