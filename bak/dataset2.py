"""
#Dataset2.py
Author 	: sblim
Date	: 2018-12-04
이 프로그램은 자료형 관련 스터디 프로그램입니다.
"""

#문자열 슬라이싱
str = "Life is too short, You need Python"

str_new = str[12] + str[13] + str[14] + str[15] + str[16] #short 단순한 방법

#slicing 기법 str[시작번호 : 끝번호] 시작번호 <= str < 끝번호
str[0:4] #Life 슬라이싱 기법

str[12:] #12번째부터 끝까지 short, You need Python


str = "20181208BirthdayMinyub"

date = str[:8] #20181208
birth = str[8:16] #Birthday
name = str[16:] #Minyub


print(date, birth, name)

#문자열 포멧팅
str = "I eat %d apples."%3 #숫자 바로 대입
print(str)
str = "I eat %s apples."%"five" #문자열 바로 대입
print(str)
number = 5
str = "I eat %d apples."%number #숫자 바로 대입
print(str)

number = 3
day = "four"
str = "I ate %d apples. so I was sick for %s days."%(number, day) #두개 이상 대입하기
print(str)

str = "Error is %d%%."%95 #%를 사용하기 위해서는 %%를 한다.
print(str)

#문자 개수 세기 (count)
str = "aaaaabbbbbccc"
str.count('b') # 5개
print(str.count('b'))

#문자 위치 알려주기 (find)
#문자열이 없으면 -1 리턴
#있으면 그 위치 숫자 리턴 0부터시작

#문자 위치 알려주기 (index)
#찾는 문자의 맨 처음 위치를 반환

#문자열 삽입하기 (join)

a = ","
print(a.join("abcd"))

#upper 대문자로
a = "hi"
print(a.upper())

#lower 소문자로
a = "HI"
print(a.lower())

#lstrip rstrip strip 공백 지우기

#replace 문자열 바꾸기
str = "Life is too short"
print(str.replace("Life", "Your leg"))

#split 문자열 나누기
str = "Life is too short"
print(str.split())

str = "a/b/c/d/e"
print(str.split('/'))
