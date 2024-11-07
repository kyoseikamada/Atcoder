N = int(input())

S = set()

for i in range(N):
    s = input()
    s_reverse = s[::-1]
    if s == s_reverse:
        s += "."
    S.add(s)
    S.add(s_reverse)

print(int(len(S)/2))
