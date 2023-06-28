n = 6  # 그래프 정점 수
g = [[]] * n
g[0] = [[1, 4], [3, 8], [4, 2]]
g[1] = [[0, 4], [2, 9], [4, 3]]
g[2] = [[1, 9], [3, 2], [5, 1]]
g[3] = [[0, 8], [2, 2], [4, 4], [5, 1]]
g[4] = [[0, 2], [1, 3], [2, 7], [3, 4]]
g[5] = [[2, 1], [3, 1]]

included = [False for _ in range(n)]     # 트리에 포함 여부
D = [float('inf') for _ in range(n)]     # 트리의 정점에서 각 정점까지의 거리
D[0] = 0
connected_to = [-1 for _ in range(n)]    # 트리의 간선을 추출하기 위해

for k in range(n):
    m = -1
    min_value = float('inf')
    for j in range(n):  # 트리 밖의 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
        if not included[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    included[m] = True
    for w, wt in g[m]:  # m에 인접하면서 트리 밖에 있는 정점의 D의 원소 갱신
        if not included[w] and wt < D[w]:
            D[w] = wt   # D 원소 갱신
            connected_to[w] = m

print('MST: ', end='')
mst_cost = 0
for i in range(1, n):
    print('(%d, %d)' % (i, connected_to[i]), end='')
    mst_cost += D[i]
print('\nMST의 가중치: ', mst_cost)
