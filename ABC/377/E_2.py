N, K = map(int, input().split())
P = list(map(int, input().split()))
ans = P.copy()


index_match_count = 0

for i in range(N):
    if P[i] == i:
        index_match_count += 1

if index_match_count == N:
    print(*P)
else:

    mod_index = N - index_match_count - 1


    if K == mod_index:
        print(*P)
    elif K > mod_index:
        if mod_index == 0:
            print(*P)
        else:
            new_K = K % mod_index
            get_k = 0

            if new_K >= N //2:
                get_k = N - new_K + 1
            else:
                get_k = new_K - 1

            for i in range(N):
                pi = P[i]
                for j in range(get_k):
                    pi = P[pi-1]
                ans[i] = pi
            
            print(*ans)
    else:
        get_k = K - 1
        for i in range(N):
            pi = P[i]
            for j in range(get_k):
                pi = P[pi-1]
            ans[i] = pi
        
        print(*ans)




