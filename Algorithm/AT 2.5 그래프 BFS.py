adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1],
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
n = len(adj_list)
visited = [False for _ in range(n + 1)]


def bfs(v):
    queue = []                   # 리스트로 큐 선언
    visited[v] = True
    queue.append(v)              # 큐에 시작점 삽입
    while len(queue) != 0:
        u = queue.pop(0)         # 큐에서 정점 v를 가져옴
        print(u, ' ', end='')    # 정점 v 출력(방문)
        for w in adj_list[u]:    # 정점 v에 인접한 방문 안된 정점에 대해
            if not visited[w]:
                visited[w] = True
                queue.append(w)  # v에 인접한 정점을 큐에 삽입


print('BFS 방문 순서:')
for i in range(n):
    if not visited[i]:
        bfs(i)

