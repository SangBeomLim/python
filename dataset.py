"""
#Dataset.py
Author 	: sblim
Date	: 2018-12-02
이 프로그램은 자료형 관련 스터디 프로그램입니다.
"""

#숫자형(Number)이란 숫자 형태로 이루어진 자료형입니다.
#for example

#Integer
a = 123;
b = -178;
c = 0;
print(a,b,c)

#Float
a = 1.2
b = 3.5
c = a + b;
print(a,b,c)

#Octal
a = 0o177
b = 0o162
c = a + b;
print(a,b,c)

#Hexadecimal
a = 0x8ff
b = 0x5ec
c = a + b;
print(a,b,c)

#Complex number
a = 1+2j
a.real 	#복소수의 실수값
a.imag	#복소수의 허수값

b = 2-1j
b.real	#복소수의 실수값
b.imag	#복소수의 허수값

c = a + b;
print(a,b,c)

'''
abs(x) 복소수 절대값 리턴
복소수.conjugate() 복소수의 켤레복소수 리턴
사칙연산 +-*/
x의 y 제곱 : x**y
나머지 연산자 :  x%y;
나눗셈 : /
나눗셈 후 나머지 제거 : //
'''
#문자열 자료형입니다
'''
"Life is too short, You need Python"
"a"
"123"
'''
food 	= "Python's favorite food is perl"
str 	= '"Python is very easy" he says.'
str2	= "Python's very easy"
str3 	= "\"Python is very easy.\"he says."
#여러줄 문자열
str = "Life is too short\nYou need python."
print(str)

multipleline = """
Life is too short
You need python
"""
print(multipleline)

multipleline = '''
Life is too short
You need python
'''
print(multipleline)


