'''
제어문 while
#control_while.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 제어문 스터디 프로그램입니다.
'''

#반복문 While

#"10번 찍어 안 넘어가는 나무 없다."

hitTree = 0

while hitTree < 10:
	hitTree += 1
	print("나무를 %d번 찍었습니다."%hitTree)
	if hitTree == 10:
		print("나무가 넘어갑니다.")
		

number = 0
while  number < 10:
	number += 1
	if number % 2 == 0: continue
	
	print(number)
	
		
#while문 직접 만들기
prompt = """
1. ADD
2. DEL
3. LIST
4. QUIT

Enter the number : """
	
number = 0

while number != 4:
	print(prompt)
	number = int(input())
	
#커피 자판기 판매량 최대 10잔, 모두 소진시 SOLD OUT 출력하고 반복문을 빠져나온다.

coffee = 10

while True :
	
	money = int(input("Input the Money : "))
	
	if money >= 300 :
		print("커피가 나옵니다.")
		coffee -= 1
		print("남은 커피 양은 %d"%coffee)
	else:
		print("돈이 부족합니다.")
		add = int(input("Input the Money : "))
		money += add
		print("돈은 %d원 있습니다. 커피가 나옵니다"%money)
		coffee -= 1
		print("남은 커피 양은 %d"%coffee)
		
	if not coffee :#coffee == 0:
		print("SOLD OUT")
		break

#break, continue문은 다른 언어랑 차이가 없다. break 루프문을 빠져나옴 continue 조건이 맞지 않으면 처음 위치로 돌아감

#무한루프 (Infinitity Loop)
#while(1) | while (true) => python while True: