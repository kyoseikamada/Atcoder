import numpy as np

N, Q = map(int, input().split())
A = list(map(int, input().split()))

np_A = np.array(A)

for i in range(Q):
    b, k = map(int, input().split())
    tmp_A = np.abs(np_A - b)
    tmp_A_sort = np.sort(tmp_A)
    print(tmp_A_sort[k-1])