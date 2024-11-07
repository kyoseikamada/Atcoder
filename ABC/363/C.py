from itertools import permutations

N, K = map(int, input().split())
S = input()

def isIn_Kaibun(s, k):
    for i in range(N-k+1):
        st = s[i:i+k]
        if st == st[::-1]:
            return True
        else:
            continue
    
    return False

count = 0

set_S = set()

for st in permutations(S):
    s = "".join(st)
    set_S.add(s)

for s in set_S:
    if not isIn_Kaibun(s, K):
        count += 1
    else:
        continue

print(count)