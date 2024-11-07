S = list(map(int, input().split()))

ans = True

if not (100<= S[0] and S[0] <= 675 and S[0] % 25 == 0):
    ans = False

for i in range(1,len(S)):
    if not(S[i] >= S[i-1]):
        ans = False
    if not (100<= S[i] and S[i] <= 675 and S[i] % 25 == 0):
        ans = False


if ans:
    print("Yes")
else:
    print("No")