S = input()

match_list = ["A", "B", "C"]

ans = True

for x in match_list:
    count = 0
    for j in range(len(S)):
        if x == S[j]:
            break
        else:
            count += 1

    if count == len(S):
        ans = False


if ans:
    print("Yes")
else:
    print("No")