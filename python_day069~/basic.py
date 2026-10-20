# [ day069 - 20261019 ]

# 파이썬 파일 만들기
## 파일명 뒤에 확장자(.py) 만든다.
# 파이썬 한줄 주석

# 56p
print("Hello Python") # shift + enter 한줄씩/문장 실행
# 파일 안에 우클릭 -> run python -> 전체 실행

# 70p
import keyword
print( keyword.kwlist )

# 77p
# 하나만 출력합니다.
print("하나만 출력합니다.")
# 여러개를 출력합니다.
print("여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("아무것도 출력하지 않습니다.")
print("---확인 전용선 ---")
print()
print()
print("---확인 전용선 ---")

# 85p
print(type("Hello Python"))                 # <class 'str'>
print(type(10))                             # <class 'int'>
print(type(3.14))                           # <class 'float'>
print(type(True))                           # <class 'bool'>
print(type([1, 2, 3]))                      # <class 'list'>
print(type((1, 2, 3)))                      # <class 'tuple'>
print(type({1, 2, 3}))                      # <class 'set'>
print(type({"name":"홍길동", "age":20}))     # <class 'dict'>
print(type(None))                           # <class 'NoneType'>
print(type(print))                          # <class 'builtin_function_or_method'>
print(type(type(10)))                       # <class 'type'>

# 86p ~ 91p
print("ABC") # 큰따옴표 감싸기
print('ABC') # 작은따옴표 감싸기
print("""A
B
C""") # 큰따옴표 3개 감싸기
print("''") # 작은따옴표 출력
print('""') # 큰따옴표 출력
print("\"A\'B\nC\tD\\E")

# 93p
# 1. + 연결연산자
print("안녕" + "하세요")
# print("안녕" + 1)    주의 : 문자열과 숫자 연결 불가능

# 2. * 반복연산자
print("안녕" * 3)

# 3. 인덱싱 , 문자열은 배열/리스트 이므로 인덱스 존재한다.
#    인덱스 : 0부터 요소들이 저장된 순서 , *음수도 가능*
print("가나디"[0])
print("가나디"[1])
print("가나디"[2])
print("가나디"[-1])
print("가나디"[-2])
print("가나디"[-3])

# 4. 슬라이싱 , 문자열 자르기/일부 추출 , [ 시작인덱스 : 끝인덱스-1 ]
print("안녕하세요반갑습니다잘부탁드려요"[5:10])
print("안녕하세요반갑습니다잘부탁드려요"[0] + "원" + "안녕하세요반갑습니다잘부탁드려요"[10:12])
#    시작인덱스 생략시 0 부터 , 끝인덱스 생략시 마지막 인덱스 까지
print("가나다라마바사아자차카타파하"[:7])
print("가나다라마바사아자차카타파하"[7:])

# 5. 문자열의 길이 , len(문자열)
print( len("안녕하세요") )

# 104p
print(5+7)
print(5-7)
print(5*7)
print(5/7)

print(3//2)
print(5%3)
print(3**2)

print(5+3*2)   # 사칙연산 우선순위 적용
print((5+3)*2) 

# 115p
# 변수명 = 값
pi = 3.141592
r = 10
# r2   초기값 없으면 NameError
# 변수 참조 : 호출
print(pi , r )
print(2*pi*r)

# 116
number = 100    # 100
number += 10    # 110
number -= 10    # 100
number *= 2     # 200
number /= 2     # 100.0
number %= 3     # 1.0
number **= 3    # 1.0
print(number)

number = "안녕하세요"
number += "!"
number *= 3
print(number)

# 118p
input("인사말 입력 >>")
string = input("타입검사 입력 >>")
print( type( string ) )     # 123 -> str , asd -> str

# 121p
string_int = int(string)
string_float = float(string)
print(type(string_int))
print(type(string_float))
string_str1 = str(string_int)
print(type(string_str1))
string_str2 = str(string_float)
print(type(string_str2))

# 125p
raw_input = input("inch 입력 >>")
inch = int( raw_input )
cm = inch * 2.54
print(cm)

# 135p
string_a = "age:{}".format(10)
print(string_a) 
string_b = "{} {} {}".format( 1 , "안녕" , True )
print(string_b)
# 주의 : {} 개수와 값의 개수는 일치해야함.

# 141p
a = "hElLo"
print(a.upper())
print(a)
print(a.lower())

# 142p
b = " h e L l o  Py t  h on "
print( b )
print( b.strip() )

# 143p
# isOOO : 보통 반환타입 True/False
print( "Hello".isalpha() ) # True
print( "Hello".isdigit() ) # False

# 144p
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
output_c = "안녕안녕하세요".find("hi")
print(output_c)     # -1 없음.

# 145p
# 찾을값 in 문자열
print("안녕" in "안녕하세요")
print("hello" in "안녕하세요")

a = "10 20 30 40 50".split(" ")     # 공백 기준으로 자르기
print( a )      # ['10', '20', '30', '40', '50']
print( a[2] )   # 30

# 146p
li = [10 , 20 , 30]
num = 10
a1 = "{} {} {}".format(*li)
a2 = f"age:{num}"
a3 = "age:10"
print(f"""{a1}
{a2}
{a3}""")

# 158p
x = 25
print(10 < x < 30)

print( not True )
print( True and True )
print( True and False )
print( True or False )

# 163p
age = 10
if age >= 19 :
    print("성인입니다.")
elif age >= 14 :
    print("학생입니다")
else :
    print("무료입니다.")

score = int(input("점수를 입력하세요 >>"))
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
else :
    print("재시험")

x = 10;
if x>5 :
    if x>10 :
        print("완전 크다")
    else :
        print("적당하다")
else :
    print("작다")


# 165p
import datetime as dt
now = dt.datetime.now()
print(now.year , "년")
print(now.month , "월")
print(now.day , "일")
print(now.hour , "시")
print(now.minute , "분")
print(now.second , "초")


# [ day070 - 20261020 ]

# 192p
# 리스트 : 대괄호[]에 자료를 쉼표로 구분하여 여러 자료들을 저장
# [ 요소 , 요소 , 요소 ]  :  요소 = element
# 인덱스 : 리스트 안에 요소들이 저장된 순서번호, 0부터 시작
list_a = [ 273, 32, 103, "문자열", True, False ]
print( list_a )
print( list_a[2] )
print( list_a[1:3] )
list_a[2] = 7
print( list_a[7] )
# 파이썬에서는 인덱싱 음수로 가능
print( list_a[-2] )
print( list_a[3][1] )
# print( list_a[1][1] )

# 195p
list_1 = [ 1, 2, 3 ]
list_2 = [ [ 1 , 2 ] , [ 3 , 4 ] , [ 5 , 6 ] ]
list_3 = [ [ [ 1 , 2 ] , [ 3 , 4 ] ] , [ [ 5 , 6 ] , [ 7 , 8 ] ] ]
# 행렬 => pandas , dataframe 활용
print(list_2[1][0])

# 196p
# 파이썬 특징 : 정형화된 데이터들을 다른 언어들과 다르게 연산이 가능함
list_a = [ 1, 2, 3 ]
list_b = [ 4, 5, 6 ]
print( list_a + list_b )
print( list_a * 3 )
print( len( list_a ) )
list_aa = [ [ 1 , 2 ] , [ 3 , 4 ] , [ 5 , 6 ] ]
print( list_a + list_aa )

# 198p
print( list_a )
list_a.append(4)
print( list_a )
list_a.insert(0 , 5)
print( list_a )
list_a.remove(2)
print( list_a )

# 주의 : 
list_c = [1,2]
list_c + [3]        # 새로운 리스트 생성
list_c.append(3)    # 기존 리스트 수정

# 202p
list_a = [1,2,3,4,5]
del list_a[1]
print( list_a )
list_a.pop(2)
print( list_a )
del list_a[0:2]
print( list_a )

list_a = [1,2,3,4,5]
list_a.remove(2)
print( list_a )
list_a = [1,2,3,2,4,5]
list_a.remove(2)
print( list_a )
list_a.clear()
print( list_a )
del list_a
# print( list_a )

# 204p
numbers = [1,2,3,4,5,6,7,8]
print( numbers[0:5:2] )
print( numbers[::-1] )

# 205p
numbers = [1,5,234,62,6,2,3]
print( sorted(numbers) )
print(numbers)
print( sorted(numbers, reverse=True) )
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 206p
list_a = [273 , 32, 103, 57, 52]
print( 52 in list_a )
print( 51 in list_a )
print( 52 not in list_a )
print( 51 not in list_a )

# 208p
for i in range(100):
    print("출력")

for element in list_a :
    print(element)

for char in "안녕하세요" :
    print(char)

list_a = [2,3,4,5,6,7,8,9]
list_b = [1,2,3,4,5,6,7,8,9]
for i in list_a :
    for a in list_b :
        print(i , " x ", a ," = ", i*a )

# 212p
list_a = [ 273, 32, 103, "문자열", True, False ]
print( *list_a )

# 217p
# 딕셔너리 : { }중괄호 선언 후   키 : 값   형태로 쉽표로 연결
# { key:value , key:value , key:value }
# key 중복 불가능
# JS : JSON , JAVA : MAP/DTO , DB : RECORD , PYTHON : DICTIONARY
dict_a = { 'name' : '어벤져스 엔드게임', 'type' : '히어로 무비' }
print( dict_a["name"] )
print( dict_a["type"] )         # 없으면 Error
# print( dict_a["price"] )
print( dict_a.get("name") )
print( dict_a.get("price") )    # 없으면 None 반환

# 221p
dict_a[ 'price' ] = 5000
print( dict_a )
dict_a[ "name" ] = '어벤져스 엔드게임.v2'
print( dict_a )
del dict_a[ 'type' ]    # 없으면 Error
print( dict_a )
dict_a.pop('price')     # 없으면 Error
print( dict_a )

dict_a = { 'name' : '어벤져스 엔드게임', 'type' : '히어로 무비' }
print( 'name' in dict_a )
print( 'price' in dict_a )

# 226p
for key in dict_a :
    print( dict_a.get(key) )
    print( dict_a[key] )

dictionary = { 
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕","메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

for key in dictionary :
    print( key , ":" , dictionary[key] )


numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers :
    output[number%3-1].append(number)

print(output)

# 231p
print( range(5) )
print( list( range( 5 ) ) )

print( list( range( 3 , 8 ) ) )

print( list( range( 0 , 10 , 2 ) ) )

# 233p
# for 와 range 함께
# 1부터 10까지 출력
for i in range(1, 11):
    print(i)

for i in range(10, 0 , -1):
    print(i)

for i in range(1, 11 , 2):
    print(i)

# 240p
i=0
while i <= 10 :
    print(i)
    i += 1 

list_a = [10, 20, 30, 10, 30]
value = 10
while value in list_a :
    list_a.remove(value)
    print(list_a)

# 244p
for i in range(1 , 11, 1) :
    print( i )
    if i == 3:
        break
for i in range(1,11,1):
    print( i )
    if i == 3:
        continue


numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers :
    if number in counter :
        counter[number] += 1
    else :
        counter[number] = 1

print(counter)

# 251p
numbers = [103,52,273,32,77]
print( min(numbers) )
print( max(numbers) )
print( sum(numbers) )

# 252p
numbers_reversed = reversed(numbers)
print( numbers_reversed )
print( next(numbers_reversed) )
print( list(numbers_reversed) )

# 264p
# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
# 이터레이터 : 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
# 이터레이터 가능한 타입 : 리스트 / 딕셔너리 / 문자열 / 튜플 등
# 이터레이터 하나씩 꺼내는 함수 : next( ) 함수 ---> 이터러블
# 즉, 이터레이터가 존재하는 자료만 for 사용가능

# 254p
numbers = [103,52,273,32,77]
print( enumerate(numbers) )
print( list( enumerate(numbers) ) )     
# [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]
# [ (index , value) , (index , value) , (index , value) ]
for index, value in enumerate(numbers):
    print(index, value)

# 256p
dict_a = { "name" : "김길리" , "age" : 10 }

print( dict_a.items() )

for key, value in dict_a.items():
    print( key, value )

# 258p
array = [ ]
for i in range( 0 , 21 , 2 ) :
    array.append( i )
print(array)

array = [ i for i in range( 0 , 21 , 2 ) ]
print(array)

array = [ i for i in range( 0 , 21 , 2 ) if i != 10 ]
print(array)

array = [ i for i in range( 0 , 21 , 2 ) if i != 10 and i != 16 ]
print(array)

# 263p
print("""안녕하세요1
안녕하세요2""")

print("안녕하세요1\n안녕하세요2")

print( ("안녕하세요1\n" "안녕하세요2") )

print( "\n".join( [ "안녕하세요1" , "안녕하세요2" ] ) )

print( "-".join( "김길리" ) )   # 전처리(텍스트마이닝) 등


print(list(range(3,10,3)))

key_list = ["a" , "b" , "c" , "d"]
value_list = [1,2,3,4]
charater = {}

a=0
for x in key_list :
    a += 1
    b = 0
    for y in value_list :
        b += 1
        if a==b :
            charater[x] = y

print(charater)


max_value = 0
a = 0
b = 0

for i in range(1,100) :
    j = 100 - i
    x = i * j
    if x > max_value :
        max_value = x
        a = i
        b = j

print( a, b , max_value)


array = [ i for i in range( 0 , 21 , 2 ) if i != 10 and i != 16 ]

output = [ i for i in range(1, 101)
          if str("{:b}".format(i)).count("0")==1]

for i in output :
    print(f"{i} : {"{:b}".format(i)}")
print("합계 : ", sum(output))




charater = {
    "name" : "기사",
    "level" : 12,
    "item" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트",
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in charater :
    if type(charater[key]) is str or  type(charater[key]) is int :
        print(f"{key} : {charater[key]}")
    if type(charater[key]) is list:
        for aa in charater[key] :
            print(f"{key} : {aa}")
    if type(charater[key]) is dict :    # charater[key] = "item" : { "sword" : "불꽃의 검", "armor" : "풀플레이트" }
        for bb in charater[key] :
                print(f"{bb} : {charater[key][bb]}")


list_a = [1,2,3,4,1,2,3,1,4,1,2,3]
dict_a = {}

for i in list_a :
    if i in dict_a :
        dict_a[i] += 1
    else :
        dict_a[i] = 1

count = 0

for i in dict_a :
    count += 1

print(len(dict_a))
print(f"""{list_a}에서
사용된 숫자의 종류는 {len(dict_a)}개입니다.""")

print(f"""{list_a}에서
사용된 숫자의 종류는 {count}개입니다.""")

print(f"참고 : {dict_a}")








dna_list = "ctacaatgtcagtatacccattgcattagccgg"
dict_a = {}

for i in dna_list :
    if i in dict_a :
        dict_a[i] += 1 
    else :
        dict_a[i] = 1

print(f"염기 서열을 입력해주세요 : {dna_list}")

for i in dict_a :
    print(f"{i}의 개수: {dict_a[i]}")

for i, value in enumerate(dict_a) :
    print(f"{i}의 개수: {dict_a[value]}")





















