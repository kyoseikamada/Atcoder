H, W, Q = map(int, input().split())

G = [[True]*W for i in range(H)]
H_isTrue = [list(range(W)) for i in range(H)]
W_isTrue = [list(range(H)) for i in range(W)]

G_kabe = H*W

for i in range(Q):
    r, c = map(int, input().split())
    r = r-1
    c = c-1

    while True:
        if G[r][c]:
            G[r][c] = False
            G_kabe -= 1
            H_isTrue[r][c] = None
            W_isTrue[c][r] = None
            break
        else:
            #上を消す
            if len(W_isTrue[c]) > 0:
                h = max(W_isTrue[c][:r])
                G[h][c] = False
                G_kabe -= 1
                H_isTrue[h][c] = None
                W_isTrue[c][h] = None

            #下を消す
            if len(W_isTrue[c]) > 0:
                h = min(W_isTrue[c][r:])
                G[h][c] = False
                G_kabe -= 1
                H_isTrue[h][c] = None
                W_isTrue[c][h] = None

            #左を消す
            if len(H_isTrue[r]) > 0:
                w = max(H_isTrue[r][:c])
                G[r][w] = False
                G_kabe -= 1
                H_isTrue[r][w] = None
                W_isTrue[w][r] = None

            #右を消す
            if len(H_isTrue[r]) > 0:
                w = min(H_isTrue[r][c:])
                G[r][w] = False
                G_kabe -= 1
                H_isTrue[r][w] = None
                W_isTrue[w][r] = None

            break

print(G_kabe)