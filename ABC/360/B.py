S , T = input().split()

ans = False

for i in range(0, len(S)-1):
    T_koho = []
    for k in range(0, len(S)-i, i+1):
        T_koho.append(S[k:k+i+1])

    if len(S) % (i+1) != 0:
        T_koho.append(S[len(S)-len(S) % (i+1):len(S)])
    
    for k in range(i+1):
        TT = ""
        for t in T_koho:
            if len(t) >= k+1:
                TT += t[k]

        if TT == T:
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")