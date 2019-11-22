'''
제어문 if
#control_if.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 제어문 스터디 프로그램입니다.
'''

#ex1) "돈이 있다면 택시를 타고, 돈이 없으면 걸어 간다."

money = 1 #TRUE 돈이 있다고 선언 0이면 돈이 없다고 선언

if money:
	print("택시를 타자.")
else:
	print("걸어 간다.")
		
		
#다른 언어와 다르게 들여쓰기가 중요함.
#들여쓰기할 때 Tab을 할 것인지? 스페이스바를 사용할 것인지?는 개발자의 자유 
#단, 현재 파이썬 개발자들은 기본적으로 스페이스바 4번을 사용한다고 한다.

#조건문 비교연산자는 다른 프로그램과 동일하다. ==, !=, <, >, <=, >=

#ex2) "만약 돈 3000원 이상이 있다면 택시를 타고, 그렇지 않다면 걸어가라."

money = 2000 #2000원을 가지고 있다.

if money >= 3000:
	print("택시를 타고 가라.")
else:
	print("걸어가라.")
	
#ex3) "만약 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고, 그렇지 않으면 걸어가라"

money = 2000 #돈 2000원 선언
card = 1 #카드가 있다

if money >= 3000 or card :
	print("택시를 타고 가라")
else:
	print("걸어 가라")

if money >= 3000 and card :
	print("택시를 타고 가라")
else:
	print("걸어 가라")
	
if not card :
	print("걸어 가라")
else:
	print("택시를 타고 가라")
	
# x in list,tuple,string
# x not in list, tuple, string
# ~있는가? ~없는가?

a = [1,2,3,4,5]

if 5 in a:
	print("5가 존재합니다.")
else:
	print("5가 존재하지 않습니다.")

if 6 not in a:
	print("6이 존재하지 않습니다.")
else:
	print("6이 존재합니다.")

#ex4) "만약 주머니에 돈이 있으면 택시를 타고, 그렇지 않으면 걸어가라"

pocket = ['paper','phone','money'] #주머니에 종이, 핸드폰, 돈이 있다고

if 'aaaa' in pocket:
	print("택시를 타고 가라~!")
elif 'paper':
	pass #해당 조건문을 실행할 때 아무일도 하지 않는다.
else:
	print("걸어가라~!")

#ex5) "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없다면 걸어가라"

pocket = ['phone','paper']
card = 1

if 'money' in pocket:
	print("버스를 타고 가라")
elif 'card' in pocket:
	print("택시를 타고 가라")
else:
	print("걸어 가라")

	

