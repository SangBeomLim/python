'''
함수
#function1.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 함수 스터디 프로그램입니다.
'''

#Function
#x->f(x)->y

#함수의 역할
#1. 반복되는 작업을 간소화 시킨다.
#2. 프로그램의 흐름을 이해하기 쉽게 만든다.
#def 함수이름(인수):
#	수행할문장

def sum(a,b):
	return a + b

a = 3
b = 4
c = sum(a,b)
print(c)


#일반적인 Function
#def function_name(input value)
#	수행문장
#	return output value

#입력값이 존재하지 않는 Function
#	return 'OUTPUT_STRING'

#결과값이 존재하지 않는 Function
# 	return (X)

#입력값, 결과값이 없는 Function

#여러 개의 인수를 가지는 함수의
#def sum_many(*args) *args = (1,2,3,4,5,6,7)

def sum_many(*args):
	sum = 0;
	for i in args:
		sum += i
		
	return sum
		

a = sum_many(1,2,3,4,5)
print(a)

def sum_mul(choice, *args):
	if choice == 'sum':
		result = 0
		for i in args:
			result += i
	
	elif choice == 'mul':
		result = 1
		for i in args:
			result *= i
			
	return result

a = sum_mul('sum',1,2,3,4)
print(a)

a = sum_mul('mul',1,2,3,4)
print(a)

def sum_and_mul(a,b):
	return a+b,a*b
	
	
result = sum_and_mul(3,4)
print(result) #7,12

sum, mul = sum_and_mul(3,4)
print(sum, mul)

#함수 인수 초기값 미리 설정하기
def intro_myself(name, old, man = True):
	print("나의 이름은 %s 입니다."%name)
	print("나의 나이는 %d 입니다."%old)
	if man:
		print("남자입니다.")
	else:
		print("여자입니다.")

intro_myself("김철수",20)
intro_myself("이영이",19,False)
intro_myself("홍길동",30,True)

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return

a = 1
def vartest(a):
	a = a + 1
	return a
	
a = vartest(3) # a = 3+1 = 4
print(a)

#2. global
a = 1
def vartest():
	global a
	a = a + 1
	
vartest()
print(a)


