s = [5, 2, 8, 6, 4, 6, 1, 9, 3]  # 입력 순서
n = len(s)  # 그래프 정점 수
g = [None, None, [0, 1], [0, 1], [1], [0, 1, 4], None, [0, 1, 2, 3, 4, 5, 6], [1]]
previous = [-1 for _ in range(n)]  # 순서 추출을 위해
length = [1 for _ in range(n)]     # 길이 초기화
for i in range(1, n):
    if g[i] is not None:
        max_length = -1
        for j in g[i]:  # 들어오는 간선의 각 끝점 j에 대해
            if length[j] > max_length:
                max_length = length[j]
                previous[i] = j
        length[i] = max_length + 1

print('가장 긴 증가 순서의 길이 =', max(length))

k = length.index(max(length))  # k는 가장 긴 길이를 가진 항목의 인덱스
seq = [k]  # 순서 역추적
while previous[k] != -1:
    seq.insert(0, previous[k])
    k = previous[k]
lis = [s[i] for i in seq ]
print('가장 긴 증가 순서 = ', lis)
