# 동전 거스름돈 알고리즘
# 201902404 윤현섭
# 테스트 케이스: price = 2550, pay = 5000인 경우
price = int(input())
pay = int(input())
charge = pay - price
print("거스름돈은 총 {0}원이다.".format(charge))

coins = [1000,500,100,50,10] # 거스름돈 액면가 종류
result = {x: 0 for x in coins} # 거스름돈 출력 -> 동전 종류: 거슬러주는 동전 개수

for coin in coins:
	coin_count = charge // coin
	charge -= coin * coin_count
	result[coin] = coin_count
 
 
print("거슬러주는 동전은 아래 와 같다. \n {0}".format(result))
print("거슬러주는 동전의 총 개수는 {0}개이다.".format(len(result.values())))