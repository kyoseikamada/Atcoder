from collections import deque

H, W = map(int, input().split())
S = []

for i in range(H):
    S.append(input())

Q = deque()

visited = [[False]*W for i in range(H)]
keiro = ["s","n","u","k","e"]

if S[0][0] != "s":
    print("No")
else:
    Q.append((0,0,0))
    visited[0][0] = True

    ans = False

    while len(Q) > 0:
        q = Q.popleft()
        x = q[0]
        y = q[1]
        s = q[2]
        
        if x - 1 >= 0:
            x_new = x - 1
            if not visited[x_new][y]:
                if S[x_new][y] == keiro[(s+1) % 5]:
                    if x_new == W -1 and y == H - 1:
                        ans = True
                        break
                    else:
                        Q.append((x_new,y,(s+1) % 5))
                        visited[x_new][y] = True

        if x + 1 <= H - 1:
            x_new = x + 1
            if not visited[x_new][y]:
                if S[x_new][y] == keiro[(s+1) % 5]:
                    if x_new == H -1 and y == W - 1:
                        ans = True
                        break
                    else:
                        Q.append((x_new,y,(s+1) % 5))
                        visited[x_new][y] = True

        if y - 1 >= 0:
            y_new = y - 1
            if not visited[x][y_new]:
                if S[x][y_new] == keiro[(s+1) % 5]:
                    if x == W -1 and y_new == H - 1:
                        ans = True
                        break
                    else:
                        Q.append((x,y_new,(s+1) % 5))
                        visited[x][y_new] = True

        if y + 1 <= W - 1:
            y_new = y + 1
            if not visited[x][y_new]:
                if S[x][y_new] == keiro[(s+1) % 5]:
                    if x == H -1 and y_new == W - 1:
                        ans = True
                        break
                    else:
                        Q.append((x,y_new,(s+1) % 5))
                        visited[x][y_new] = True

        
    if ans:
        print("Yes")
    else:
        print("No")