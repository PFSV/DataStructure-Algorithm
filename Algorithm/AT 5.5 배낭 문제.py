W = [5, 4, 6, 3]
V = [10, 40, 30, 54]
K = 10   # 배낭의 용량
n = len(W)
T = [[0 for _ in range(K+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(K+1):
        if W[i] > j:
            T[i][j] = T[i-1][j]
        else:
            T[i][j] = max(T[i-1][j], V[i] + T[i-1][j - W[i]])

print('최대 가치:', T[n-1][K])

'''
V = [20, 5, 10, 40, 15, 25]
W = [1, 2, 3, 8, 7, 4]
W = [5, 4, 6, 3]
V = [10, 40, 30, 50]
K = 10
W = [2, 5, 10, 5]
V = [40, 30, 50, 10]
K = 16
W = [1, 11, 21, 23, 33, 43, 45, 55]
V = [11, 21, 31, 33, 43, 53, 55, 65]
K = 110  # 159
'''