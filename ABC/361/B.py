a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

x1 = set(range(a,d+1))
y1 = set(range(b,e+1))
z1 = set(range(c,f+1))

g1 = set(range(g,j+1))
h1 = set(range(h,k+1))
i1 = set(range(i,l+1))

xg = x1&g1
yh = y1&h1
zi = z1&i1

ans = False

if len(xg) >= 2 and len(yh) >= 2 and len(zi) >= 2:
    ans = True



if ans:
    print("Yes")
else:
    print("No")