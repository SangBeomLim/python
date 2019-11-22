"""
#List.py
Author 	: sblim
Date	: 2018-12-04
이 프로그램은 리스트 관련 스터디 프로그램입니다.
"""

#리스트 자료형
'''
리스트를 만들 때 대괄호 [ ] 사용
리스트명 = [요소1, 요소2, 요소3,...]
'''

a = [] #void 리스트
b = [1,2,3] #int형 리스트
c = ['Life', 'is', 'too', 'short'] #문자형 리스트
d = [1, 2, 'Life', 'is'] #숫자, 문자형 리스트
e = [1,2,['Life','is']] #숫자, 리스트를 가진 리스트

e[0] #1
e[1] #2
e[2] #['Life','is']
e[2][0] #Life
e[2][1] #is

#삼중리스트인 경우
# a[x][y][z]

# Indexing and Slicing of List
a = [1,2,3] #1,2,3을 원소로 가지는 리스트
a[0] + a[2] #1+3 = 4
a[-1] # 3

a = [1,3,5,7,9]

print(a[0:2]) #1,3 0<=a<2

a = [1,2,['a','b','c','d'],3,4,5,['a','b','c']]
'''
a[0] = 1 & a[1] = 2 & a[2] = ['a','b','c','d'] & a[3] = 3 & a[4] = 4 & a[5] = 5 & a[6] = ['a','b','c']
'''

print(a[2][:3]) # 'a','b','c'
print(a[6][1:]) # 'b','c'

#리스트 더하기(+)
str1 = ["andy", "lion", "python", "start"]
str2 = ['end', 'shutdown', 'exit']

print(str1+str2) #[andy, lion, python, start, end, shutdown, exit]

str1 = ['andy', 'lion', 'start', 'python']

#리스트 반복하기(*)
print(str1*3)
number = 3
#정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬 내장 함수
print(str(number))

#modify of list
a = [1,2,3]
a[2] = 4 # 3->4 modified
print(a)

#Modified continuous range of list
a[1] = ['a','b','c']
print(a)
a[1:2] = ['a','b','c']
print(a)

#Remove an element of list using [] 
a[1:3] = []
print(a)

#Remove an element of list using del
del a[1]
print(a)

#append()
a = [1,2,3] 
a.append(4) #[1,2,3,4]
print(a)
a.append([5,6]) #[1,2,3,4,[5,6]]
print(a)

#sort()
a = [1,4,3,6,7,2,5]
a.sort() #a 정렬하기
print(a)

#reverse()
a = ['c','b','a']
a.reverse() # a=['a','b','c']
print(a)

#return to position (index)
a = [1,5,2,4,3]
print(a.index(3)) #a[4] return value is 4

#insert(a[x], x) x = element, a[x] = position
a = [1,2,3]
a.insert(0,4) # a[0] = 4, a = [4,1,2,3]
print(a)
a.insert(3,5) # a[3] = 5, a = [4,1,2,5,3]
print(a)

#remove(x) x = element
a.remove(5) # a[3] = 5, a = [4,1,2,3]
a.remove(3) # a[3] = 3, a = [4,1,2]

#pop(x) x = element
print(a.pop()) #2
print(a.pop(0)) #4
print(a)

#count(x) x = element
a = [1,2,3,1,1,1,1,1]
print(a.count(1)) #1 of element count

#extend(x) x = element
a = [1,2,3,4]
b = [6,7]
a.extend(b) # a += b || a = a + b

print(a)
 

