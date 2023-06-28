from heapq import heappush, heappop, heapify


def huffman_tree(a):
    h = [[freq, [char, ""]] for char, freq in a]  # ""에 코드 담는다.
    heapify(h)  # 최소 힙 만들기
    while len(h) > 1:
        left = heappop(h)       # 루트 제거(최소의 빈도수 가진 항목 제거)
        right = heappop(h)      # 한번 더 루트 제거
        for code in left[1:]:   # 왼쪽 자식이면 0 추가
            code[1] = '0' + code[1]
        for code in right[1:]:  # 오른쪽 자식이면 1 추가
            code[1] = '1' + code[1]
        t = [left[0] + right[0]] + left[1:] + right[1:]  # 합쳐진 새 항목
        print(t)
        heappush(h, t)          # 힙에 새 항목 t 삽입
    return h  # 힙 h는 1개의 항목만 가진채 리턴


input_freq = [['b', 20], ['c', 30], ['d', 35], ['e', 40], ['a', 60], ['f', 90]]

h_code = huffman_tree(input_freq)

result = sorted(heappop(h_code)[1:], key=lambda x: x)
for ch, code in result:
    print(ch, ':', code)
