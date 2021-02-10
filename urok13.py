n = int(input())
A = [0] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
ans = 0
for j in range(n):
    ans += A[0][j]
    ans += A[n-1][j]
    ans += A[j][0]
    ans += A[j][n-1]

ans -= A[0][0]
ans -= A[0][n-1]
ans -= A[n-1][0]
ans -= A[n-1][n-1]
print(ans)