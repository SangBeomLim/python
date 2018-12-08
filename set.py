'''
집합 자료형
#set.py
Author 	: sblim
Date	: 2018-12-08
이 프로그램은 Set 스터디 프로그램입니다.
'''

#집합(SET)은 파이썬 2.3버전부터 지원하기 시작한 자료형
#s1 = set([1,2,3]) #{1,2,3}
#s2 = set("HELLO") #{'H','E','L','O'}

#특징 
#1. 중복을 허용하지 않는다.
#2. 순서가 없다. 인덱싱을 사용할 수 없다.

#인덱싱을 사용하기 위해서
#리스트로 변환
#LIST = list(s1)
#튜플로 변환
#TUPLE = tuple(s2)

#집합 자료형 활용하기
#교집합
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])

s3 = s1&s2
print(s3) #{3,4}
s3 = s1.intersection(s2)
print(s3) #{3,4}

#합집합
s3 = s1 | s2 
print(s3) #{1,2,3,4,5,6}
s3 = s1.union(s2)
print(s3)

#차집합
s3 = s1 - s2 #s3 = s1.difference(s2)
print(s3) #{1,2}
s3 = s2 - s1 #s3 = s2.difference(s1)
print(s3) #{5,6}

#ADD 1개 원소 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

#UPDATE 여러 개 원소 추가
s1 = set([1,2,3])
s1.update([5,6,7])
print(s1) #{1,2,3,5,6,7}

#REMOVE 특정 원소 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1) #{1,3}

