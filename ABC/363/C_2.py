import itertools

N, K = map(int, input().split())
S = input()

count = 0

set_S = set()

for st in itertools.permutations(S):
    s = "".join(st)
    set_S.add(s)
    is_kai = False
    for i in range(N-K+1):
        st = s[i:i+K]
        if st == st[::-1]:
            is_kai = True
            break
    if not is_kai:
        count += 1

print(count)