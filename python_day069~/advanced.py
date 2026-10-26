# [ day073 - 20261023 ]

# 기술면접 키워드 
# 절차지향 프로그래밍 : 데이터를 순서대로 처리하고 하향식 순차 실행 흐름 , C 언어
# 객체지향 프로그래밍 : 객체들의 상호작용으로 프로그래밍 설계 , JAVA PYTHON JS
# 관점지향 프로그래밍 : 공통되는 기능(로그,검증,보안)들을 분리하여 프로그래밍 설계 , SPRING
# 추상화 : 핵심적인 개념 또는 기능을 간추려 내는 것
# 객체 : 속성명과 속성값으로 표현 , [ list ] { dictionary }
# 클래스 : 추상화한 데이터들을 구조화 한 것 ( like 설계도 )
# 생성자 : 객체 생성할 때 사용하는 , 객체를 초기화하는 함수 
# 객체 : 세상에 존재하는 모든 데이터들을 추상화 ( 실체 X )                - 개념적 객체
# 인스턴스 : 추상화한 것을 실체로 만든 것 ( 실체 O , 메모리가 생겼으면 O )  - 물리적 객체
# 인스턴스화 : 컴퓨터 안에 객체 정보를 저장하는 것.  JAVA : new 생성자( )  ,  PYTHON : 생성자( )
# 생성자 : 클래스 기반으로 인스턴스를 만드는 함수  ->  인스턴스 초기화 함수
# GC (가비지컬렉터) : 더 사용할 가능성이 없는 데이터를 자동으로 제거해주는 역할
# 상속 :
# 다중상속 :
# 오버로딩 :
# 오버라이딩 :

# 466p
# 클래스 만들기
class Student :
    pass

student = Student( )   # JAVA : new Student( )  ,  PYTHON : Student( )

student = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()
]

class Student2 : 
  # def __init__(self , 멤버변수1 , 멤버변수2, 멤버변수3 ) : 
  #     self.멤버변수1 = 멤버변수1
    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science

    def get_average( self ) :
        return self.get_sum() / 4

    def to_string( self ) :
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

# 일반 함수와 메소드의 차이
# 일반 함수는 클래스 밖에서 독립 선언 / 메소드는 클래스 안에서 선언
# 일반 함수에서는 self 가 없고, 메소드에서는 self 가 있다.
def get_sum2() :
    pass


# 생성자 이용한 인스턴스 생성
# JAVA 에서는 아래처럼
# Student2 s = new Student2("김길리", 10, 20, 30, 40)
students = [
    Student2("김길리", 87, 97, 68, 86),
    Student2("홍길동", 78, 79, 98, 87),
    Student2("가나디", 87, 84, 49, 97),
    Student2("마우스", 86, 90, 67, 66),
    Student2("키보드", 67, 47, 68, 86),
    Student2("삼다수", 97, 77, 68, 66)
]

# 인스턴스 안에 멤버변수 호출
print( students[0].korean )

for student in students :
    print( student.to_string() )


# 475p

# 상속 : 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것
# isinstance( 인스턴스 , 클래스명 )
class Student :
    def __init__(self):
        pass

class Human : 
    def __init__(self):
        pass

student = Student()
print( isinstance( student , Student ) )  # True
print( isinstance( student , Human ) )    # False


# 478p
class Student2 : 
  # def __init__(self , 멤버변수1 , 멤버변수2, 멤버변수3 ) : 
  #     self.멤버변수1 = 멤버변수1
    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science

    def get_average( self ) :
        return self.get_sum() / 4

    def to_string( self ) :
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드
    # 보조기능 재정의( 오버라이딩 )
    def __str__(self):
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드 / 비교 메소드
    # 총합계 비교 함수 재정의
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()


students = [
    Student2("김길리", 100 , 100, 100, 100), Student2("김길리", 100 , 100, 100, 100),
    Student2("가나디", 87, 84, 49, 97), Student2("마우스", 86, 90, 67, 66),
    Student2("키보드", 67, 47, 68, 86), Student2("삼다수", 97, 77, 68, 66)
]

# 특수한 이름의 메소드 호출 , str( 인스턴스 )  vs  str( )  
# 재정의 하지 않으면 주소값 또는 문자열을 반환하는 함수 
print( str( students[0] ) )  # __str__ 함수 실행된다.

print( students[0] == students[1] )     # 주소값이 다름. but  == 의 의미를 재정의함. ==>>  __eq__ 
print( students[0] != students[1] )     # 주소값이 다름. but  != 의 의미를 재정의함. ==>>  __ne__


# 484p
class Student2 : 
  # def __init__(self , 멤버변수1 , 멤버변수2, 멤버변수3 ) : 
  #     self.멤버변수1 = 멤버변수1

    count = 0

    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
      # 클래스변수 호출 방법 : 클래스명.변수명
        Student2.count += 1  

    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science

    def get_average( self ) :
        return self.get_sum() / 4

    def to_string( self ) :
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드
    # 보조기능 재정의( 오버라이딩 )
    def __str__(self):
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드 / 비교 메소드
    # 총합계 비교 함수 재정의
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()


students = [
    Student2("김길리", 100 , 100, 100, 100), Student2("김길리", 100 , 100, 100, 100),
    Student2("가나디", 87, 84, 49, 97), Student2("마우스", 86, 90, 67, 66),
    Student2("키보드", 67, 47, 68, 86), Student2("삼다수", 97, 77, 68, 66)
]


# 클래스명.변수명 : 클래스변수 값 호출
print( Student2.count )

# 인스턴스.메소드()  a.sum()  :   클래스.메소드()  A.sum()

# 486p
# 클래스 함수
class Student2 : 
  # def __init__(self , 멤버변수1 , 멤버변수2, 멤버변수3 ) : 
  #     self.멤버변수1 = 멤버변수1

    count = 0
    students = [ ]

    @classmethod        # 클래스 함수 정의하는 데코레이터/어노테이션
    def print( cls ) :  # 매개변수에 cls 관례적으로 선언
        for student in cls.students :  # cls.클래스변수  <=동일=>  클래스명.클래스변수
            print( str( student ) )

    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
      # 클래스변수 호출 방법 : 클래스명.변수명
        Student2.count += 1  

    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science

    def get_average( self ) :
        return self.get_sum() / 4

    def to_string( self ) :
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드
    # 보조기능 재정의( 오버라이딩 )
    def __str__(self):
        return "{} /t {} /t {}".format( self.name , self.get_sum() , self.get_average() )

    # 특수한 이름의 메소드 / 비교 메소드
    # 총합계 비교 함수 재정의
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()



students = [
    Student2("김길리", 100 , 100, 100, 100), Student2("김길리", 100 , 100, 100, 100),
    Student2("가나디", 87, 84, 49, 97), Student2("마우스", 86, 90, 67, 66),
    Student2("키보드", 67, 47, 68, 86), Student2("삼다수", 97, 77, 68, 66)
]

# 클래스명.클래스함수
Student2.print( )


# 491p
import math

class Circle : 
    def __init__(self , radius):
        self.__radius = radius      # JAVA : private int radius
        self.__radius2 = radius

    def get_circumference( self ) :
        return 2*self.__radius
    def get_radius(self) :
        return self.__radius
    def set_radius(self , radius) :
        self.__radius = radius

    # setter and getter 자동생성
    @property
    def radius2( self ) :
        return self.__radius2

    @radius2.setter
    def radius2( self , value ) :
        self.__radius2 = value

circle = Circle( 10 )
try :
    print( circle.__radius )  # 클래스 외부에서 프라이빗 변수 사용 불가.
except :
    pass
    
print( circle.get_circumference() )
print( circle.get_radius() )
print( circle.set_radius( 5 ) )

print( circle.radius2 )
circle.radius2 = 20
print( circle.radius2 )

# 497p
# 상속의 활용
# 파이썬은 부모클래스가 여러개 가능 , 상속을 여러개 받을 수 있음
class Parent : 
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스 __init__ 메소드 호출")
    def test(self) :
        print("Parent 클래스의 test 메소드 호출")

class Child(Parent) : 
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init() 메소드 호출")
    def test(self) :    # 오버라이딩/재정의
        print("Child 클래스의 test 메소드 호출")

child = Child()
child.test()
print(child.value)

parent = Parent()
parent.test()

parent2 = child
parent2.test()

# JAVA 에서는 타입으로 혼동이 올 수 있지만 오버라이딩 우선 이라고 생각하면 편함.

# 505p
class Student :
    def __init__(self, name, score) :
        self.name = name
        self.score = score

class StudentList :
    def __init__(self) :
        self.students = [ ]
    def append(self, student) :
        # students.append(student)
        self.students.append( student )
    def get_average(self) :
        total = 0
        for i in self.students :
            total += i.score
        return total / len(self.students)
    def get_first_by_score(self) :
        first = 0
        index = 0
        find_index = 0
        for i in self.students :
            if i.score > first :
                first = i.score
                find_index = index
            index += 1
        return self.students[find_index]
    def get_last_by_score(self) :
        last = 0
        index = 0
        find_index = 0
        for i in self.students :
            if i.score < last :
                last = i.score
                find_index = index
            index += 1
        return self.students[find_index]

students = StudentList()
students.append(Student("구름", 100))
students.append(Student("별", 49))
students.append(Student("초코", 81))
students.append(Student("아지", 90))

print(f"{students.get_average()}")
print(f"{students.get_first_by_score().name}")
print(f"{students.get_last_by_score().name}")


class Stack :
    def __init__(self):
        self.list = [ ]
    def push(self, item) :
        self.list.append(item)
    def pop(self) :
        a = self.list[len(self.list)-1]
        self.list.pop()
        return a


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print( stack )
print( stack.pop() )
print( stack.pop() )
print( stack.pop() )


class Queue :
    def __init__(self):
        self.list = [ ]
    def enqueue(self, item) :
        self.list.append(item)
    def dequeue(self) :
        a = self.list[0]
        self.list.pop(0)
        del self.list[0]
        return a

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
