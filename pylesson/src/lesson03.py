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
a = [1,2,3,4]
a.append(5) #요소 추가
print(a)
a.append([2,3])
print(a)

#2. 리스트 정렬 (sort)
a = [1,5,6,7,3,2,4,3]
print(a)
a.sort()
print(a)

#3. 리스트 뒤집기 (reverse)
a = [1,4,3,2,6]
a.reverse()
print(a)

#4. 위치 반환 (index) 리스트의 인덱스 넘버 반환
a = [1,2,3,4,5]
print(a.index(1)) #0
print(a.index(4)) #3
#print(a.index(7) #error message

#5. 리스트에 요소 삽입 (insert)
a = [1,2,3,4]
a.insert(0, 4) #a[0]위치에 4 삽입 [4,1,2,3,4]
print(a)
a.insert(3, 7) #a[3]위치에 7삽입 결과 : [4,1,2,7,3,4]
print(a)

#6. 리스트에서 삭제 (remove) remove(x) x가 가장 먼저나오는 리스트 요소 삭제
a.remove(7)
print(a)
a.remove(4)
print(a)

#7. 리스트 요소 꺼내기 (pop) 리스트에서 가장 마지막 요소 꺼내고 삭제하기
a = [1,2,3,4]
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)

#8. 리스트에 포함된 요소 x의 개수 카운트 (count)
a = [1,2,1,2,1,1,1,7]
print(a.count(1))   #요소 1의 개수 세기
print(a.count(2))   #요소 2의 개수 세기

#9. 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)
b = [7,8]
a.extend(b)
print(a)
