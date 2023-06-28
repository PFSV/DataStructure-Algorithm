BIN_SIZE = 10  # 통의 용량
item = [7, 5, 6, 4, 2, 3, 7, 5]  # 입력: 물건들의 크기
n = len(item)   # 물건의 수
bins = [[] for i in range(n)]  # bins[0]:첫 번째 통, bins[1]:두 번째 통 ...
remnant = [BIN_SIZE for _ in range(n)]  # 각 통의 남는 부분
bin_count = 1

for i in range(n):  # 물건 i를 통에 담기
    j = 0  # 첫 번째 통
    packed = False
    while j < bin_count:  # 물건 i를 기존의 통 j에 넣으려는 시도
        if item[i] <= remnant[j]:
            bins[j].append([i, item[i]])
            remnant[j] -= item[i]
            packed = True
            break
        j += 1  # 디음 통
    if not packed:  # 새 통에 물건 i를 넣는다.
        bins[j].append([i, item[i]])
        remnant[j] -= item[i]
        bin_count += 1

print('최초 적합: 총 사용된 통의 수  =', bin_count)
for i in range(bin_count):
    print('통 %d: ' % i)
    for j in range(len(bins[i])):
        print(' 물건 = %d, size = %d ' % (bins[i][j][0], bins[i][j][1]))

