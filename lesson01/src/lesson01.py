#Lesson01. 파이썬 기초 자료형
#Author : Andy Lion
#Date   : 2019-11-22

#Number
#Integer (정수형)
a = 123 #양의 정수 123을 a에 대입
print(a)
a = -123 #음의 정수 123을 a에 대입
print(a)

#Float or Double (실수형)
a = 1.2
print(a)
a = -3.2
print(a)

#지수 표기
a = 3.14E10 #3.14 * 10^10
print(a)
a = 3.14e-10 #3.14 * 10^-10
print(a)

#Octal (8진수)
a = 0o177
print(a)

#Hex (16진수)
a = 0x16f
print(a)

#복소수
a = 4 + 5j
print(a)

#복소수.real (복소수의 실수부)
print(a.real)

#복소수.imag (복소수의 허수)
print(a.imag)

#복소수.conjugate() (복소수의 켤레복소수)
print(a.conjugate())

#abs(복소수) 절대값을 리턴
print(abs(a))

#사칙연산 (+, -, *, /)
n1 = 5
n2 = 7
print('덧셈 : ', n1+n2) # + 더하기 12
print("뺄셈 : ",n1-n2) # - 빼기 -2
print("곱셈 : ", n1*n2) # * 곱하기 35
print("나눗셈 : ", n1/n2) # / 나누기 0.71...

#지수승 연산 x**y ==> x^y
n1 = 2
n2 = 8
print(n1**n2) #n1^n2 2^8 = 256

#나머지 연산 %x
print(n1%n2) #2

#나머지를 버리는 나눗셈 연산 //
print(2//8) #0


