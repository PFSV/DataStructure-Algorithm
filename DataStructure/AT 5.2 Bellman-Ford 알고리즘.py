INF = float('inf')
graph = [[INF, 3, 4, INF, INF, INF, INF],
         [INF, INF, INF, 1, INF, INF, INF],
         [INF, INF, INF, INF, 2, INF, INF],
         [INF, INF, INF, INF, 4, -1, INF],
         [INF, -4, INF, INF, INF, INF, 3],
         [INF, INF, INF, INF, INF, INF, 1],
         [INF, INF, INF, INF, INF, INF, INF]]
n = len(graph)  # 그래프 정점의 수

s = 0  # 출발점
D = [INF for _ in range(n)]
D[s] = 0
previous = [-1 for _ in range(n)]
previous[s] = 0
for k in range(n - 1):  # n-1회 반복
    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF:
                if D[j] > D[i] + graph[i][j]:
                    D[j] = D[i] + graph[i][j]  # 간선 완화
                    previous[j] = i  # i 덕분에 j까지 거리가 단축됨
# 결과 출력
print('정점 %1d으로부터의 최단 거리' % s)
for i in range(n):
    print('[%d, %d] = %3d' % (s, i, D[i]))
print()

print('정점 0으로부터의 최단 경로')
for i in range(n):
    back = i
    print(back, end='')
    while back != 0:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()
