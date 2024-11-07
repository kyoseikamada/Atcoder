import itertools

N, M = map(int, input().split())

S = []

for i in range(N):
    S.append(input())



max_tast = 0

for i in range(N):
    k = S[i].count("o")
    if k > max_tast:
        max_tast =k


count = 1000

if max_tast == 1:
    print(M)
else:
    for v in itertools.permutations(S):
        if v[0].count("o") < max_tast:
            next
        else:
            test = [0]*M
            for i, k in enumerate(v):
                for j in range(M):
                    if k[j] == "o":
                        test[j] = 1
                
                if sum(test) == M:
                    count_koho = i+1
                    if count > count_koho:
                        count = count_koho
                        break
                    else:
                        break
                elif i >= count:
                    break

    print(count)