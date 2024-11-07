N, K = map(int, input().split())

R = list(map(int, input().split()))

ans = []

def roop(depth, tmp):
    for i in range(1, R[depth]+1):
        tmp[depth] = i
        if depth != N-1:
            roop(depth+1, tmp)
        else:
            if sum(tmp) % K == 0:
                koho = tmp.copy()
                ans.append(koho)

roop(0,[0]*N)

for i in range(len(ans)):
    print(*ans[i])
        
