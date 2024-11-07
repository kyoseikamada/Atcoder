S = []

for i in range(8):
    s = input()
    S.append(s)


ans = 0

for i in range(8):
    for j in range(8):
        if S[i][j] == ".":
            S_i = S[i]
            is_Put = True
            for k in range(8):
                if S_i[k] == "#":
                    is_Put = False
                    break
            
            for k in range(8):
                if S[k][j] == "#":
                    is_Put = False
                    break
            
            if is_Put:
                ans += 1

print(ans)
