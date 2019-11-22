#Lesson02. 파이썬 기초 자료형
#Author : Andy Lion
#Date   : 2019-11-22

#String
#문자, 단어 등으로 구성된 문자들의 집합
#This is my house
#I am a student
#on the 4 floor

a = 'hello world'
print(a) #' '작은 따옴표로 만들기
a = "python is good"
print(a) #" "큰 따옴표로 만들기
a = """hello, python!!""" #""" """ 큰 따옴표로 만들기
print(a)
a = '''type is string''' #''' ''' 작은 따옴표로 만들기
print(a)
a = "python's very easy!" # " " 안에 작은 따옴표 구성하기
print(a)
a = '"python is very easy." he say' # ' ' 안에 큰 따옴표를 추가하여 문자열 구성하기
print(a)
a = '" \"python\'s very easy! \" " he say' # \' or \" 를 사용하여 문자열에 따옴표 추가하기
print(a)
a = "'python\'s very easy!'\n he say." # \n을 사용하여 다음 줄로 출력하기
print(a)

str1 = "python"
str2 = " is very easy!"
print(str1 + str2)  #문자열 연결하기
print(str1*3) #문자열 곱하기

#문자열 곱하기 사용 예제
print("=" * 50)
print("Python Basic Programming lesson")
print("=" * 50)

#문자열 인덱싱
a = "python is very easy!" #p:0 y:1 t:2 h:3 o:4 n:5 i:7 s:8 v:10 e:11 r:12 y:13 e:15 a:16 s:17 y:18 !:19
for i in range(0, 19):
    print(a[i]) #양의 정수는 정방향 음수는 반대방향

#문자열 슬라이싱
a = "python is very easy!" #p:0 y:1 t:2 h:3 o:4 n:5 i:7 s:8 v:10 e:11 r:12 y:13 e:15 a:16 s:17 y:18 !:19
b = a[0] + a[1] + a[2] + a[3] + a[4] + a[5]
print(b) #python
b = a[10:14] # 10<= x < 14 10, 11, 12, 13
print(b) #very
b = a[15:] # 15<= x <=end
print(b) #easy

string_ = "20191122PM11:00SunFriday" #year-string[:4] month-string[4:6] day-string[6:8] time-string[8:15] weather-string[15:18] day-str[18:]
year = string_[:4]
month = string_[4:6]
day = string_[6:8]
time = string_[8:15]
weather = string_[15:18]
day_str = string_[18:]

print("year : ", year) #2019
print("month : ", month) #11
print("day : ", day) #22
print("time : ", time) #PM11:00
print("weather : ", weather) #SUN
print("day_str : ", day_str) #Friday

#String Format
a = "I eat %d apples."%3 #숫자 포멧
print(a)
a = "I eat %s apples."%"three" #문자 포멧
print(a)
number = 5
a = "I eat %d apples."%number #변수 포멧
print(a)
a = "%s is very easy. I eat %d apples."%("python", number) #두개 이상의 다른 포멧 대입
print(a)
#Special String Format {0}, {1}, {2}
a = "{0} is {1}. {2} is very {3}".format('p', 3.14, 'python', 'easy')
print(a)

a = "HI."
print("%-10s"%a) #왼쪽 정렬
print("%10s"%a) #오른쪽 정렬

#문자열 관련 함수들
#1. 문자 개수 세기 (count)
a = "%s is very easy. I eat %d apples."%("python", number)
print(a.count('p')) #a 문자열에 존재하는 p의 개수 3
#2. 문자 위치 검색 (find)
print(a.find('e')) #a 문자열에 존재하는 최초의 e 위치 검색 11
print(a.find('z')) #만약 문자열에 검색 값이 존재하지 않는다면 -1리턴
#3. 문자 위치 검색2 (index)
print(a.index('e'))
#print(a.index('z')) #원하는 인덱스가 없으면 에러 발생

#4. 문자열 삽입 (join)
b = ","
c = b.join("abcdefg")
print(c)
#5. 소문자를 대문자로
c = a.upper()
print(c)

#6. 대문자를 소문자로
print(c.lower())

#7. 왼쪽 / 오른쪽 / 양쪽 공백 지우기
b = "    hi  "
b.lstrip() #왼쪽 공백 지우기
b.rstrip() #오른쪽 공백 지우기
b.strip() #양쪽 공백 지우기

#8. 문자열 바꾸기 (replace)
print(a)
print(a.replace("python", "hello world"))

#9. 문자열 나누기 (split)
print(a.split()) #공백 기준으로 문자열 나누기
b = "a:b:c:d"
c = "a,b,c,d"
print(b.split(':')) # : 기준으로 문자열 나누기
print(c.split(',')) # , 기준으로 문자열 나누기


#TODO



