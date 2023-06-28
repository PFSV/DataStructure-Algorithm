def valid(i):
    for j in range(n):  # 색칠 검사
        if g[i][j] and color[i] == color[j] and (color[i] != -1):
            return False
    return True


def coloring(i):
    if i == n:
        print('색칠 결과:', color)  # 해 출력
        return True

    for c in range(K):
        color[i] = c  # 색을 c로 시도
        if valid(i):
            if coloring(i + 1):
                return True
    return False


g = [[0, 1, 0, 1, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [0, 1, 0, 1, 0, 0],
     [1, 1, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 1],
     [1, 1, 0, 0, 1, 0]]
n = len(g)
K = 3  # 색의 수: 색은 0, 1, 2
color = [-1 for i in range(n)]  # -1로 초기화
if not coloring(0):
    print('색칠 할 수 없음')


'''
Ptersen Graph
g = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]]
    '''