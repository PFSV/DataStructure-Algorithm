a = [['문학회', 9.0, 11.0], ['지역봉사회', 9.0, 12.5], ['서예회', 13.0, 14.5],
     ['바둑회', 14.0, 17.0], ['미술회', 11.0, 14.0], ['사진회', 9.0, 11.0],
     ['음악회', 15.0, 16.5], ['창조회', 15.0, 16.5], ['독서회', 11.0, 12.5],
     ['토론회', 13.0, 14.5]]

n = len(a)
a.sort(key=lambda x: x[1])  # 시작 시간으로 정렬
solution = [[a[0]]]
finish_time = [a[0][2]]  # 직전 선택된 동아리 미팅 종료 시간
k = 0  # 미팅룸0
for i in range(1, n):
    flag = False
    for j in range(k+1):
        if a[i][1] >= finish_time[j]:  # 현재 동아리 a[i]를 미팅룸 j에
            solution[j].append(a[i])   # 할당 가능하면 solution[j] 뒤에 추가
            finish_time[j] = a[i][2]   # 미팅룸[j]의 finish_time 갱신
            flag = True                # 다음 동아리를 위해 for-루프로
            break
    if not flag:  # 새 미팅룸 만들기
        k += 1
        solution.append([a[i]])
        finish_time.append(a[i][2])

for i in range(k+1):
    print('미팅룸', i+1, ':', solution[i])
