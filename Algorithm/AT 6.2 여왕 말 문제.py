def is_threatening(i, j):
    for k in range(n):    # 행과 열 검사
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    for k in range(n):    # 대각선 검사
        for l in range(n):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    return False


def queen(i):
    if i == n:   # 모든 말을 다 배치했으면
        return True
    for j in range(n):
        if (not(is_threatening(i, j))) and (board[i][j] != 1):
            board[i][j] = 1
            if queen(i + 1):    # 다음 여왕 말을 위해 순환 호출
                return True
            board[i][j] = 0     # board[i][j]에 배치 실패로 초기화
    return False


print("여왕 말의 수: ", end='')
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
queen(0)

for x in board:  # 결과 출력
    print(*x, sep="  ")

