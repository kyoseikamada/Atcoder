S = input()

ans = False

R = S.find("R")
M = S.find("M")

if R < M:
    ans = True


if ans:
    print("Yes")
else:
    print("No")