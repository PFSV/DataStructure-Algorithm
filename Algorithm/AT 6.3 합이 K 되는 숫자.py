def promising(i, current_sum, leftover):
    if i == -1:
        return True
    else:
        return (current_sum + leftover >= K) and \
               (current_sum == K or current_sum + S[i+1] <= K)  # 다음 숫자 추가하여 K를 초과하지 말아야


def find_set(i, current_sum, leftover):      # current_sum 은 현재까지 포함시킨 숫자들의 합
    if promising(i, current_sum, leftover):  # leftover 는 아직 고려하지 않은 숫자들의 합
        if current_sum == K:
            return True
        else:
            include[i+1] = True    # S[i+1] 포함
            if find_set(i+1, current_sum + S[i+1], leftover - S[i+1]):
                return True

            include[i+1] = False   # S[i+1] 포기
            if find_set(i+1, current_sum, leftover - S[i+1]):
                return True
    return False


S = [15, 20, 55, 75]  # 미리 정렬됨, S.sort()
K = 95
n = len(S)
include = [None for _ in range(n)]
if find_set(-1, 0, sum(S)):  # -1은 상태 공간 트리에서 S[0]을 아직 고려하지 않은 상태 의미
    print([S[j] for j in range(n) if include[j]])
else:
    print('답 없음')

#S =[267, 493, 869, 961, 1000, 1153, 1246, 1598, 1766, 1922]
#K = 5842  K = 869+961+1000+1246+1766

#S = [518533, 1037066, 2074132, 1648264, 796528, 1593056, 686112, 1372224, 244448, 488896,
#     977792, 1955584, 1411168, 322336, 644672, 1289344, 78688, 157376, 314752, 629504, 1259008]
#S.sort()
#K = 2463098 #  0 1 0 0 1 0 0 0 0 0, 0 0 0 0 0 0 0 0 0 1, 0: 1037066+796528+629504 = K

#print('i=', i, 'current_sum=', current_sum, 'S[i]=', S[i], 'leftover=', leftover)