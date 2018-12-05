"""
#tuple.py
Author 	: sblim
Date	: 2018-12-06
이 프로그램은 tuple 스터디 프로그램입니다.
"""

'''
튜플은 리스트와 거의 동일하다.
차이점 
리스트 [] 튜플 ()
리스트는 생성, 삭제, 수정이 가능
튜플은 불가능

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','bc'))
'''

tuple = (1, 2,'andy','lion','python', 'start')

#del tuple[0] #error occured
#tuple[0] = 4 #error occured

#indexing is find
print(tuple[3]) #'andy'

#slicing is range find
print(tuple[1:]) # 2,'andy','lion','python', 'start'

#plus
tuple2 = (4,5)
tuple += tuple2
print(tuple)
#multiple
print(tuple2*2)



