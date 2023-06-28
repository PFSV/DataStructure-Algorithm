n = 8  # 그래프 정점 수
s = 0  # 시작점
g = [[]] * n
g[0] = [[1, 3], [3, 5], [4, 6]]
g[1] = [[2, 3], [3, 1], [5, 4]]
g[2] = [[3, 7]]
g[3] = [[4, 4], [5, 1]]
g[4] = [[5, 8], [6, 1]]
g[5] = [[2, 6], [7, 10]]
g[6] = [[5, 9], [7, 1]]
g[7] = []

included = [False for _ in range(n)]   # 초기화
distance = [float('inf') for _ in range(n)]  # distance[i]를 최댓값으로 초기화
distance[s] = 0
previous = [-1 for _ in range(n)]      # 최단 경로를 추출하기 위해
previous[s] = 0

for k in range(n):
    m = -1
    min_value = float('inf')
    for j in range(n):  # 방문 안된 정점들의 distance 원소들 중에서 최솟값을 가진 정점 m 찾기
        if not included[j] and distance[j] < min_value:
            min_value = distance[j]
            m = j
    included[m] = True

    for w, wt in g[m]:  # m에 인접한 방문 안된 각 정점의 D의 원소 갱신
        if not included[w] and distance[m] + wt < distance[w]:
            distance[w] = distance[m] + wt  # 간선 완화
            previous[w] = m

print('정점 ', s, '(으)로부터 최단 거리:')
for i in range(n):
    if distance[i] == float('inf'):
        print(s, '와(과) ', i, ' 사이에 경로 없음.')
    else:
        print('[%d, %d]' % (s, i), '=', distance[i])

print('\n정점  ', s, '(으)로부터의 최단 경로')
for i in range(n):
    back = i
    print(back, end='')
    while back != s:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()
