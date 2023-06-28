tree = [[1], [0, 3], [3], [1, 2, 4, 5], [3], [3, 6], [5]]  # MST 인접 리스트
n = len(tree)  # 그래프 정점 수
INF = float('inf')
g = [[0, 2, INF, 5, INF, INF, 5],
     [2, 0, 5, 3, INF, 6, 8],
     [INF, 5, 0, 1, 5, INF, INF],
     [5, 3, 1, 0, 2, 2, INF],
     [INF, INF, 5, 3, 0, 6, 10],
     [INF, 6, INF, 2, 6, 0, 3],
     [5, 8, INF, INF, 10, 3, 0]]
visited = [False for _ in range(n)]  # 방문되면 True 로
path = []  # 방문 순서


def dfs(v):
    visited[v] = True
    path.append(v)
    for w in tree[v]:
        if not visited[w]:
            dfs(w)
            path.append(v)


dfs(0)
print('트리 방문 순서:', path)
s = []
for vertex in path:  # 이미 방문된 점을 리스트에서 제거
    if vertex not in s:
        s.append(vertex)
s.append(0)
print('TSP 경로:', s)

distance = 0
for i in range(n):  # 경로 길이 계산
    distance += g[s[i]][s[i+1]]
print('경로 길이 = ', distance)

