S = input()
T = input()


if len(S) != len(T):

    min_moji = min(len(S), len(T))

    ans = -100

    for i in range(min_moji):
        if S[i] != T[i]:
            ans = i+1
            break
        else:
            continue
    
    if ans != -100:
        print(ans)
    else:
        print(min_moji+1)
else:
    if S == T:
        print(0)
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                print(i+1)
                break
            else:
                continue