'''
딕셔너리 자료형
#Dictionary.py
Author 	: sblim
Date	: 2018-12-06
이 프로그램은 Dictionary 스터디 프로그램입니다.
'''

#연관배열(Associative Array) or 딕셔너리(Dictionary)
#{Key1 : Value1, Key2 : Value2, Key3 : Value3, ...}

#sblim dictionary
dic = {'name' : 'sblim', 'age' : '37', 'birth' : '8xxxxx', 'phone' : '010xxxxxxxx'}

'''
name = sblim
age = 37
birth = 8xxxxx
phone = 010xxxxxxxx
'''

#Pair Add / Delete

a = {1 : 'a'}
a[2] = 'b' #{2 : 'b'}

del a[1]

dic = {"kim" : "피겨", "ryu" : "야구", "park" : "축구", "lim" : "파이썬"}

print(dic)

print(dic['kim'])

#keys()
print(dic.keys())
#values()
print(dic.values())
#items()
print(dic.items())
#get()
print(dic.get('lim'))
#clear()
print(dic.clear())

#get(x, default) if x not, run default

#in 조사하기 
print('lim' in dic)
