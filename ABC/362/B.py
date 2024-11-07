xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

ax = xa - xb
ay = ya - yb
bx = xb - xc
by = yb - yc
cx = xc - xa
cy = yc - ya

if ax*bx + ay*by == 0:
    print("Yes")
elif ax*cx + ay*cy == 0:
    print("Yes")
elif bx*cx + by*cy == 0:
    print("Yes")
else:
    print("No")