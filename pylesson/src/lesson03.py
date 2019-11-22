#Lesson02. 파이썬 기초 자료형
#Author : Andy Lion
#Date   : 2019-11-23

#리스트 (List)
# List_Name = [element1, element2, element3, ....]

a = [] #empty list
print(a)
b = [1,2,3] #1,2,3 element in list
print(b)
c = ['life', 'is', 'too', 'short'] #life, is, too, short in list
print(c)
d = [1, 2, 'in', 'list'] #1,2,in,list in list
print(d)
e = [1, 2, ['in', 'list']] #1,2,['in', 'list'] in list
print(e)

#리스트 인덱싱 (list indexing)
a = [1,2,3]
print('{0}, {1}, {2}'.format(a[0],a[1],a[2]))
#인덱스의 합 (special string format)
print('{0} + {1} + {2} = {3}'.format(a[0], a[1], a[2], a[0]+a[1]+a[2]))
#인덱스의 차 (string format)
print('%d - %d = %d'%(a[2], a[0], a[2]-a[0])) #a[0] = 1, a[1] = 2, a[2] = 3
print('%d - %d = %d'%(a[-1], a[-3], a[2]-a[-3])) #a[-1] = 3, a[-2] = 2, a[-3] = 1

#이중 리스트 인덱싱(double list indexing)
a = [1,2,[3,4,5]]
print(a[2][2]) #5
print(a[2]) #[3,4,5]
print(a[2][0]) #3
#삼중 리스트 인덱싱(triple list indexing)
a = [1,2,[3,4,5,[6,7,8,9]]]
print(a[2][3][3]) #9
print(a[2][3]) #[6,7,8,9]
#리스트 슬라이싱 (list slicing)
a = [1,2,3,4,5]
print(a[0:3]) #0<=x <3 ==>1,2,3
print(a[0:1]) #1
print(a[2:]) #3,4,5
print(a[:3]) #1,2,3

a = [1,2,[3,4,[5,6,7]]]
b = a[2][0:] #3,4,[5,6,7]
c = a[2][2][:2] #5,6
print(b)
print(c)

#리스트의 합 (list1 + list2)
#리스트는 더하기 연산을 통해 리스트들을 하나의 집합으로 만들 수 있음
a = [ 1,2,3,[1,2]]
b = [5,6,[5,6,7,[8,9,0]]]
print(a + b)

#리스트의 곱 (list*n)
#리스트를 n개만큼 인덱스를 증가
a = [1,2,3,[4,5]]
print(a * 5) #5배로 증가

#리스트 요소 수정
a = [1,2,3,[1,2]]
a[3][1] = 4
print(a)
a[3] = 5 #[1,2] ==> 5
print(a)
#리스트 요소 삭제
a[2:3] = []
print(a)
del a[1] #객체 삭제 함수 파이썬에 사용되는 모든 자료형
print(a)

#리스트 관련 함수
#1. 리스트에 요소 추가 (append)
