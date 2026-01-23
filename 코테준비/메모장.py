# print("컴퓨터공학과,20220832,김영조")
# a = int(input("투입한 돈:"))
# b = int(input("물건값:"))
# c = a - b
# print("거스름돈:", c)
# d = c // 500     # 500으로 나누어서 몫이 500원짜리의 개수
# c = c % 500      # 500으로 나눈 나머지를 계산한다
# e = c // 100     # 100으로 나누어서 몫이 100원짜리의 개수
# c= c % 100      # 100으로 나눈 나머지를 계산한다
# f = c // 50      # 50으로 나누어서 몫이 50원짜리의 개수
# c = c % 50       # 50으로 나눈 나머지를 계산한다
# g = c // 10      # 10으로 나누어서 몫이 10원짜리의 개수
# print("500원 동전의 개수:", d)
# print("100원 동전의 개수:", e)
# print("50원 동전의 개수", f) #f 출력
# print("10원 동전의 개수",g)  #g 출력

ftemp = int(input("화씨 온도:"))
ctemp = (ftemp - 32) * 5 / 9
print("섭씨 온도:", ctemp)  

print(2020 > 2030)         # False 출력
print(2020 < 2030)         # True 출력
print(2020 == 2030)        # False 출력
print(2020 != 2030)        # True 출력
print(2020 >= 2020)        # True 출력
print(2020 <= 2020)        # True 출력
print('security' == 'security')  # True 출력
print('security' != 'security')  # False 출력
print(2020 == 2020.0)      # True 출력
print(2020 is 2020.0)      # False 출력
print('a' < 'b')           # True 출력
print('ab' < "abc")        # True 출력

a = int(input('첫 번째 수를 입력하세요 : '))   # 예: 20 입력
b = int(input('두 번째 수를 입력하세요 : '))   # 예: 30 입력
print('-' * 40)

print('a = ', a, ":", bin(a))                  # a = 20 : 0b10100 출력
print('b = ', b, ":", bin(b))                  # b = 30 : 0b11110 출력

print('a & b = ', a & b, ":", bin(a & b))      # a & b = 20 : 0b10100 출력
print('a | b = ', a | b, ":", bin(a | b))      # a | b = 30 : 0b11110 출력
print('a ^ b = ', a ^ b, ":", bin(a ^ b))      # a ^ b = 10 : 0b1010 출력
