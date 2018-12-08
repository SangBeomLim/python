'''
자료형의 참과 거짓
#bool.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 BOOL 스터디 프로그램입니다.
'''

#참과 거짓
#문자열 "python" : TRUE / "" : FALSE
#숫자열 0이 아닌 수 : TRUE / 0 : FALSE
#리스트, 튜플, 딕셔너리는 비어 있지 않다면 : TRUE / 비어 있다면  : FALSE

#ex] a = [1,2,3,4]
example = [1,2,3,4]

while example:
	print(example)
	example.pop() #4->3->2->1->''

	
print(example)
	
if example == [] : 
	print("TRUE")
else :
	print("FALSE")

	
	
#메모리에 생성된 변수 없애기
a = "python "
b = "is easy"

print(a+b)

del(a)
del(b)

#리스트 복사

a = [1,2,3]

b = a #a를 b로 복사

a[1] = 4 #a and b는 같은 객체를 가리키므로 하나만 수정해도 같은 값을 출력한다

print(a, b) 

#[:] 리스트 복사 다른 객체
b = a[:] #전체 복사

a[1] = 2

print(a,b)

from copy import copy
b = copy(a)

print(a, b)

print(b is a)



