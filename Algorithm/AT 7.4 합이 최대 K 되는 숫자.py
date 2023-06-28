def filtering(A, d):
    A.sort()     # 리스트 정렬
    F = [A[0]]   # 첫 숫자를 대표 숫자로 선택
    rep_num = A[0]
    for j in range(1, len(A)):
        if A[j] > (rep_num * (1 + d)):
            F.append(A[j])   # 대표 숫자*(1+d)보다 크면 A[j]를 남기고
            rep_num = A[j]   # A[j]를 새 대표 숫자로
    return F


S = [-1, 1110, 1008, 1250, 1006]  # S[0]은 사용 안함
K = 2500
n = len(S)
epsilon = 0.4
delta = epsilon/(2*n)
T = [[0] for _ in range(n)]
for i in range(1, n):
    # T[i-1]과 [T[i-1]+S[i]]를 합병, 중복 제거
    T[i] = list(set(T[i-1]) | set([x+S[i] for x in T[i-1]]))
    T[i] = filtering(T[i], delta)  # 대표 숫자 * (1+delta)와 같거나 작으면 제거
    T[i] = [x for x in T[i] if x <= K]   # K보다 큰 수 제거

print('마지막 숫자 리스트:', T[n-1])
print('근사해 =', max(T[n-1]))
