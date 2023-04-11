N = int(input())
A = list(map(int, input().split()))
Q = int(input())


for i in range(Q):
    u, k, *x = map(int, input().split())
    if u == 1:
        A[k - 1] = x[0]
    else:
        print(A[k - 1])

