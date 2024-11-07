N = int(input())
H = list(map(int, input().split()))

ans = []

for i in range(N):
    count = 0
    for j in range(i+1, N):
        if j == i+1:
            count += 1
        else:
            h = H[i+1:j+1]
            flag = True
            for k in range(len(h)):
                if h[k] > H[j]:
                    flag = False
                    break
            
            if flag:
                count += 1
    
    ans.append(count)

print(*ans)