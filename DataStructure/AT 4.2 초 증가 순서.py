S = [1, 4, 7, 13, 26, 64, 125, 260, 550]
K = 85

solution = []
i = len(S) - 1
while K > 0:
    if S[i] <= K:  # S[i]가 K보다 크지 않으면
        solution.append(S[i])   # S[i] 추가
        K -= S[i]
    i -= 1

print(solution)
