R, G, B = map(int, input().split())
C = input()

if C == "Blue":
    print(min(R, G))
elif C == "Red":
    print(min(G, B))
else:
    print(min(R, B))