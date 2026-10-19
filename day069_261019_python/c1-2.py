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
