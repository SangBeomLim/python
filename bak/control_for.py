'''
제어문 for
#control_for.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 제어문 스터디 프로그램입니다.
'''

#For Sentence

#for value in list(or tuple, string)

list = ['one','two','three','four','five']

for i in list:		
	print(i)
	if i == 3:
		break

#다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
	print(first + last)
	

#"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격과 불합격 결과를 보여주는 프로그램을 만들어라."

marks = [90,80,50,30,100]
number = 0
for mark in marks:

	number = number + 1
	if mark < 60 : continue
	
	print("%d 학생 축하합니다. 합격입니다." %number)
	

#for와 함께 자주 사용하는 range 함수
#a = range(10) 0,1,2,3,4,5,6,7,8,9 10미만인 숫자 
#a = range(x,y) x<= a < y

#"for와 range를 사용하여 구구단을 출력하자"
#구구단은 2단부터 시작하고 각 단은 9까지 제공한다.
#range (2,9) range(1,9)를 사용하는

for i in range(2,10):
	for j in range(1,10):
		print("%d X %d = %d"%(i,j,i*j))
	print(' ')
	

#result = [표현식(num*3) for num in list 조건문(if num%2==0)]
 


