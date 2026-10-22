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



# [ day071 - 20261021 ]

list_a = [1,2,[3,4],5,[6,7],[8,9]]

list_b = []

for i in list_a :
    if type(i) == list :
        for j in i :
            list_b.append(j)
    else :
        list_b.append(i)

print(list_b)

# ++ 
def make_1chawon_list( a ) :
    if type(a) == list :
        for b in a :
            make_1chawon_list(b)
    else :
        list_b.append(a)
    
make_1chawon_list(list_a)

print(list_b)

list_str = str(list_a)
# print(list_str)
list_s = list_str.split(",")
# print(list_s)
# print(list_s[0])
for i in list_s :
    for j in i :
        if j == "[" :
            continue
        if j == "]" :
            continue
        if j == " " :
            continue
        if j.isdigit :
            list_b.append(int(j))
        else :
            list_b.append(j)

print(list_b)
    

# 275p

# 함수 : 코드의 집합
# 매개변수 : 함수를 호출할 때는 괄호 내부에 여러가지를 넣는 변수
# 리턴값 : 힘수를 호출해서 최종적으로 나오는 결과

# 값 재사용 : 변수 , 코드 재사용 = 반복문/함수

def print_3_times( ) :
    print("hi")
    print("hi")
    print("hi")

print_3_times()

# 함수 : 식별자 O  ,  반복문 : 식별자 X

# 276p
def print_n_times( value , n ) :
    for i in range( n ) :
        print( value )

print_n_times("안녕" , 5)

# 인수/인자값 : 함수 호출할 때, 매개변수에 전달하는 값

# 278p
# def 함수명( 매개변수 , 매개변수 , *가변매개변수 ) :
# 가변매개변수 조건 : 가장 뒤에 존재 , 1번만 사용
def print_n_times2( n , *values ) :
    for i in range( n ) :
        for value in values :
            print( value )
        print( )

print_n_times2( 3 , "안녕" , "hi" , "hello" )
print_n_times2( 2 , "안녕" , "hi" )

# 279p
def print_n_times3( value , n=2 ) :
    for i in range( n ) :
        print( value )

print_n_times3( "hi1" )
print_n_times3( "hi2" , 3 )

# 280p 
# 기본 매개변수가 가변 매개변수보다 앞에 올 때, ( n=2 , *value )
# 가변 매개변수가 기본 매개변수보다 앞에 올 때, ( *value , n=2 )
# 해결방안 : 키워드 매개변수
print( "안녕하세요1" )
# end 매개변수는 출력 이후 무엇을 할지
# 기본값 : end = "\n"
print( "안녕하세요2" , end = "\n" )
print( "안녕하세요3" , end = "" )
print( "안녕하세요4" , end = "" ) 

def print_n_times4( *values , n=2 ) :
    for i in range( n ) :
        for value in values :
            print(value)
        print()

print_n_times4( "hi" , "hello" , "kkk" , n=3 )
print_n_times4( "hi" , "hello" , "kkk" , 10 )

# 285p
def return_test() :
    print("A 위치 입니다.")
    return  # 함수 종료
    print("B 위치 입니다.")

return_test()

def return_test2() :
    return 100 # 함수 종료

return_test2()

def return_test3() :
    return # 함수 종료

value = return_test3()

print(value)

# 287p
def sum_all(start , end) :
    output = 0
    for i in range(start , end +1) :
        output += i
    return output

print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))

def sum_all(start=0 , end=100 , step=1) :
    output = 0
    for i in range(start , end +1 , step) :
        output += i
    return output

print("A.", sum_all(0,100,10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

# 293p
def factorial( n ) :
    output = 1
    for i in range(2 , n+1):
        output *= i
    return output

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))

def factorial2( n ) :
    if n == 1 :
        return 1
    else : 
        return n * factorial2(n-1)

print("1! : ", factorial2(1))
print("2! : ", factorial2(2))
print("3! : ", factorial2(3))
print("4! : ", factorial2(4))
print("5! : ", factorial2(5))


# gugudan
for dan in range( 2 , 10 , 1 ) :
    for gob in range( 1 , 10 , 1 ) :
        print( dan , " * " , gob , " = " , dan * gob )

def gugudan( dan=2 , gob=1 ) :
    if dan > 9 :
        return
    if gob > 9 :
        gugudan(dan+1, 1)
        return
    print( dan , " * " , gob , " = " , dan * gob )
    gugudan(dan , gob+1)
        
gugudan()

# 297p ~ 
# 피보나치수열
# 전위순회 중위순회 후위순회 레벨순회


# 317p
# 튜플 : 여러 자료들을 저장하는 리스트와 비슷한 자료형
# 특징 : 초기화 이후 수정 불가능
# 사용처 : 읽기모드용 VO , 수정 없는 자료 ( 리스트보다 메모리성능 좋음 ) 
tuple_test = (10, 20, 30)
tuple_test[0]
tuple_test[1]
tuple_test[2]
# tuple_test[0] = 1

tuple_test2 = [273]
tuple_test3 = (273)
tuple_test4 = (273,)
print(tuple_test2 , tuple_test3 , tuple_test4)

tuple_test5 = 10, 20, 30, 40
tuple_test6 = 273,
print(tuple_test5 , tuple_test6)

(a , b) = (10, 20)
print(a , b)
a , b = 10 , 20
print(a , b)
print(10 ,20)

a , b = b , a
print(a , b)

# 함수/연산 결과 항상 1개
def test() : 
    return 10,20 # 결과 1개 (10 과 20 튜플로 묶은 튜플 1개)

# 322p
# 콜백함수 : 함수 그 자체를 매개변수로 전달하여 전달받은 곳에서 전달받은 함수 호출
def call_10_items( func ) :
    func()

def print_hello() :
    print("안녕하세요")

call_10_items( print_hello() )
call_10_items( print_hello )

# 323p
# java : 리스트.stream.forEach() , 리스트.stream.map() , 리스트.stream.filter()
# react : 리스트.forEach() , 리스트.map() , 리스트.filter
# python : for x in 리스트 , map( 코드 , 리스트 ) , filter( 코드 , 리스트 )
# forEach 단순반복(return X) , map 반복+반환(return O) , filter 반복+조건반환
def power( item ) :
    return item * item
def under_3( item ) :
    return item < 3

list_a = [1,2,3,4,5]
print( list( map( power , list_a ) ) )

print( list( filter( under_3 , list_a ) ) ) 

# 324p
# 람다 : 코드 줄이기
# lambda 매개변수 : 리턴값
power = lambda x : x*x
output_a = map( power , list_a )
# 인라인 람다
output_a = map( lambda item : item*item , list_a )


list_input_a = [1,2,3,4,5]

output_a = map(lambda x : x*x , list_input_a )
print(output_a)
print(list(output_a))
print()

output_b = filter(lambda x: x<3 , list_input_a )
print(output_b)
print(list(output_b))



numbers = [1,2,3,4,5,6]
print("::".join( map( str , numbers ) ) ) 

numbers = list(range(1, 10+1))

print(list(filter( lambda x : x%2 != 0  , numbers )))

print(list(filter( lambda x : x >= 3 and x<7 , numbers )))

print(list(filter( lambda x : x**2 < 50 , numbers )))

pp = 100
mi = 2
ma = 10
memo = {}

def aaa( x , y ) :
    
    key = str( [x,y] )

    if key in memo :
        return memo[key]

    if x < 0 :
        return 0

    if x == 0 :
        return 1

    count = 0

    for i in range(y , ma+1) :
        count += aaa(x-i , i)
    memo[key] = count

    return count

print(aaa(pp,mi))

# aaa( 10 , 2 )
# key = str( [10,2] )   key = "[10,2]"
# if key in memo :  False
# if x < 0 :        False
# if x == 0 :       False
# count = 0
# for i in range(2 , 10+1) :
#     count += aaa(10-2, 2)

    # aaa( 8 , 2 )
    # key = str( [8,2] )   key = "[8,2]"
    # if key in memo :  False
    # if x < 0 :        False
    # if x == 0 :       False
    # count = 0
    # for i in range(2 , 10+1) :
    #     count += aaa(8-2, 2)

        # aaa( 6 , 2 )
        # key = str( [6,2] )   key = "[6,2]"
        # if key in memo :  False
        # if x < 0 :        False
        # if x == 0 :       False
        # count = 0
        # for i in range(2 , 10+1) :
        #     count += aaa(6-2, 2)

            # aaa( 4 , 2 )
            # key = str( [4,2] )   key = "[4,2]"
            # if key in memo :  False
            # if x < 0 :        False
            # if x == 0 :       False
            # count = 0
            # for i in range(2 , 10+1) :
            #     count += aaa(4-2, 2)

                # aaa( 2 , 2 )
                # key = str( [2,2] )   key = "[2,2]"
                # if key in memo :  False
                # if x < 0 :        False
                # if x == 0 :       False
                # count = 0
                # for i in range(2 , 10+1) :
                #     count += aaa(2-2, 2)

                    # aaa( 0 , 2 )
                    # key = str( [0,2] )   key = "[0,2]"
                    # if key in memo :  False
                    # if x < 0 :        False
                    # if x == 0 :       True
                    #   return 1

                #     count += aaa(2-3 , 2)  # False
                #     count += aaa(2-4 , 2)  # False
                #     count += aaa(2-5 , 2)  # False
                #     count += aaa(2-6 , 2)  # False
                #     count += aaa(2-7 , 2)  # False
                #     count += aaa(2-8 , 2)  # False
                #     count += aaa(2-9 , 2)  # False
                #     count += aaa(2-10, 2)  # False

                # memo[key] = count         memo = { [2,2] : 1 }
                # return count


총인원 = 100
테이블당최소인원 = 2
테이블당최대인원 = 10
중복간단해결메모 = {}

def 테이블배정경우의수( 현재남은인원 , 테이블배정인원 ) :

    메모작성 = str( [현재남은인원, 테이블배정인원] )
    
    if 현재남은인원 == 0 :
        return 1    # 가능한 경우의 수 , 카운트 O
    if 현재남은인원 < 0 :
        return 0    # 불가능한 경우의 수 , 카운트 X

    count = 0

    for 테이블에앉힐인원 in range( 테이블배정인원 , 테이블당최대인원+1 ) :

        result = 테이블배정경우의수( 현재남은인원-테이블에앉힐인원 , 테이블에앉힐인원 )

        count += result

    중복간단해결메모[메모작성] = count

    return count

테이블배정경우의수( 총인원 , 테이블당최소인원 )



# [ day072 - 20261022 ]

# 365p
# TypeError:
# ValueError:
a = input("정수 입력>> ")

if a.isdigit() :
    int_a = int(a)
    print(int_a + 2)
else :
    print("정수가 아님")

# 367p
b = input("정수 입력>> ")

try :
    int_b = int(b)
    print(int_b + 2)
except :
    print("정수가 아님")

# 368p
c = input("정수 입력 : ")
try :
    int(c)
except :
    pass  # 일단 넘어가기

# 369p
d = input("정수 입력 : ")
try : 
    int(d)
except : 
    print("정수가 아닙니다.")
else : 
    print("정수가 맞습니다.")

# 370p
e = input("정수 입력 : ")
try :
    int(e)
except :
    print("예외 발생했을 때 실행")
else :
    print("예외 발생하지 않았을 때 실행")
finally :   # 주로 외부 연결 종료시 사용
    print("무조건 실행")


# 374p
try :
    file = open("info.txt", "w")    # w 옵션 : 파일이 없으면 생성
    예외.발생코드()
    print("파일 닫기 1")
    file.close()    # 파일 닫기
except :
    print("오류 발생")
finally :
    print( "닫기 확인 1" , file.closed )
    print( "파일 닫기 2" )
    file.close()    # 파일 닫기
    print( "닫기 확인 2" , file.closed )

# 376p ~ 378p
# finally 실무 코드
# return 함수종료 or break 반복문종료 이후 무조건 실행코드 만들기.

# output = 10 + "개"
# int("하이")
# cursor.close)
# [1,2,3,4,5][10]


# 384p
# 예외객체 : 발생한 예외정보 갖는 객체
# 예외클래스 : Exception( 예외 최상위클래스 )
# except 예외클래스명 as 변수명
# as 키워드 : 클래스의 객체변수 생성
# raise : 강제로 예외발생 , 주로 CRUD 실패500 의미
list_number = [52, 273, 32, 72, 100]

try :
    number_input = int( input("정수 입력 >> ") )
    print( list_number[ number_input ] )
except Exception as e :
    print( e )

# 386p
list_number = [52, 273, 32, 72, 100]

try :
    number_input = int( input("정수 입력 >> ") )
    print( list_number[ number_input ] )
except ValueError as e :
    print( e )
except IndexError as e :
    print( e )
except Exception as e :
    print( e )

# 391p
list_number = [52, 273, 32, 72, 100]

try :
    number_input = int( input("정수 입력 >> ") )
    print( list_number[ number_input ] )
    raise NotImplementedError
except Exception as e :
    print( e )


# ++
# 346p
a = 1

def test( ) :
    global a    # 단순 호출이면 global 생략 가능
    b = a
    a = 2
    print(f"a={a}, b={b}")

print(f"global_a={a}")
test()
print(f"global_a={a}")

a = 1

def test( a) :
    b = a
    a = 2
    print(f"a={a}, b={b}")

print(f"global_a={a}")
test(a)
print(f"global_a={a}")

