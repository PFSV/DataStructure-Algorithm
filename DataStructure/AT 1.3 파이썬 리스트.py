a = []                  # empty 리스트 선언
b = [None] * 10         # 크기가 10이고 각 원소가 None 으로 초기화된 리스트
c = [40, 10, 70, 60]    # 4개의 정수로 초기화된 리스트
print(c[0])             # c의 첫 원소 출력
print(c[-1])            # c의 마지막 원소 출력
c.pop()                 # c의 마지막 원소 삭제
print(c)
c.pop(0)                # c의 첫 원소 삭제
print(c)
c.append(90)            # c의 맨 뒤에 90 추가
print(len(c))           # 내장 함수 len()은 리스트의 크기를 리턴

