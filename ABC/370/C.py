S = input()
T = input()

tmp = []

X = []


for i in range(len(S)):
    if S[i] != T[i]:
        tmp.append(True)
    else:
        tmp.append(False)

while True:
    for i in range(len(tmp)):
        if tmp[i]:
            if S[i] > T[i]:
                S = S[:i] + T[i] + S[i+1:]
                X.append(S)
                tmp[i] = False
            else:
                count = 0
                for j in range(i+1, len(tmp)):
                    if not tmp[j]:
                        count += 1
                if count == len(tmp)-(i+1):
                    S = S[:i] + T[i] + S[i+1:]
                    X.append(S)
                    tmp[i] = False

    if tmp.count(False) == len(tmp):
        break

print(len(X))
for i in range(len(X)):
    print(X[i])