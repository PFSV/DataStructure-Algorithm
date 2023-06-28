a = [['지역봉사회', 8, 13], ['서예회', 9, 11], ['토론회', 10, 12], ['바둑회', 11, 14],
     ['문학회', 13, 16], ['독서회', 14, 15], ['사진회', 15, 17]]
a.sort(key=lambda t: t[2])

solution = [a[0]]
i = 0
for j in range(1, len(a)):
    if a[j][1] >= a[i][2]:  # 직전에 선택된 동아리의 종료시간 이후에 시작하면
        solution.append(a[j])
        i = j

print('선택된 동아리:', solution)
