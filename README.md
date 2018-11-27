# 초간단 파이썬 문법 마스터하기

[목차](#index)
- Python Settings
  - Python 3.7 install
  - VSCode install
  - Python IDE
- VSCode Settings
  - format
  - CodeRunner
- Output
  - using "print"
  - Variable
  - compare & boolean
- String
  - (", ', \, \n)
  - upper
  - lower
  - strip
  - find
  - replace
- Math
- Conditinal Statement
- and, or, not
- Loop
- Function

----

## Output

1. using "print"

```
print("Hello World!!")
```
> **Result**
> Hello Wrold!!

> 파이썬에서는 print( ) 명령어로 문자열이나 변수등을 출력할 수 있다.

```
a = 10
b = 20
print(a)
print(b)
```
> **Result**
> 10
> 20



## 파이썬 객체

Class와 Instance의 이해

Class라는 상자안에 변수와 함수등을 저장한다고 생각하면 됩니다.

변수는 그릇이라고 생각하면 되고 변수타입은 그 그릇의 종류라고 생각하면 된다.

변수타입 | 변수 
------- | ------- 
int | value -> 정수형
float  | value -> 실수형
char | value -> 문자형
string | value -> 문자열형


우리는 객체가 만들어지는 것을 인스턴스라고 사용한다.
함수라는 말 대신 메소드라는 말을 사용한다.
변수는 속성, 필드, 상태라는 말로 사용할 수 있다.

-----
##### 클래스를 사용한 예제 해보기 - **계산기 프로그램** ([참고] 생활코딩)

#### 기본 클래스 생성 및 초기화 방법
```
  #Cal 클래스 생성
  class Cal(object):
  
    #constructor(생성자)
    def __init__(self, ar1, ar2):
      print(ar1, ar2)
```
> 위의 Cal 클래스가 실행되어질때 자동으로 _init_메소드 부분이 실행되어지게 된다.
> 즉, Cal 클래스 실행시 _init_메소드가 **초기화** 된다.

> **self**의 사용
> Python에서 메소드 매개변수 대응시 첫번째 매개변수는 메소드의 두번째 인자를 나타낸다!!
> 그렇기 때문에 self 매개변수를 사용하여 대응을 맞춰준다. (뒤에 자세한 설명)
> Cal(10, 10) 클래스 실행시 _init_메소드의 매개변수에 대응된다.
> **ar1 -> 10, ar2 -> 10**

#### 클래스와 메소드 사용 방법
```
  #Cal클래스에 값을 넣고 변수에 저장
  
  c1 = Cal(10, 10)
  print(c1.add()) #더하기
  print(c1.subtract()) #빼기
  
  c2 = Cal(30, 20)
  print(c2.add())
  print(c2.subtract())
```

#### add(), subtract() 메소드의 사용
```
  #Cal 클래스 생성
  class Cal(object):
  
    #constructor(생성자)
    def __init__(self, ar1, ar2):
      self.ar1 = ar1
      self.ar2 = ar2
    def add(self):
      return self.ar1+self.ar2
    def subtract(self):
      return self.ar1-self.ar2
```

**[중요]**
파이썬은 클래스를 사용할때 그 클래스를 복제한 후
초기화 메소드를 사용한다. __init__ 의 첫번째 매개변수에 우리가 생성한 인스턴스가 들어오도록 약속되어진다(**파이썬의 중요한 규칙**) 그리고 두번째 매개변수 부터 우리가 정한 값들이 들어가게 된다.

위의 ``` def add(self): ``` 에서 self는 자동적으로 현재 사용하는 인스턴스를 가리키게 된다.

----
#### 객체지향을 사용하는 이유
> 프로그램이 커짐을로써 발생하는 복잡성을 완화시키기위한 이유가 있으며 꼭 객체지향적인 알고리즘을 구상할 필요는 없다.
> 그러나, 객체지향을 사용함으로써 각각의 인스턴스에 소속성을 부여할 수 있다.
> **예를들어 아래의 코드를 보자**
```
  #LikeLion에 소속되어 있는 학생이라는 소속성을 넣을 수 있다.
  
  def LikeLion(object):
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def name(self):
      return self.name
    def age(self):
      return self.age


  student1 = LikeLion.new("준영", 25)
  student2 = LikeLion.new("주환", 26)
  student3 = LikeLion.new("선영", 23)

  print(student1.name()) #준영
  print(student1.age()) #25
  
```

 > 간단한 객체의 사용이었습니다.
 
## 파이썬 객체와 변수 (편집중 by 이주환)

## 객체 지향 프로그래밍 대표 키워드 5가지
> 1. Class(클래스) + Instance(객체)
> 2. 추상화 (Abstract)
> 3. 캡슐화 (Encapsulation)
> 4. 상속 (Inheritance)
> 5. 다형성 (Overriding)

앞서 설명한 클래스와 객체를 더욱 자세히 설명하려 한다.  
중복된 내용이 나와도 다시 한번 상기한다는 마음으로 봐주길 바란다.

### 1. 클래스와 객체

클래스(Class) = 추상(Abstract) = 타입(type) | 객체 or 오브젝트(Object) = 실체(instance) = 변수(variable)
--------- | -----------
공통 특징 | 구체
서술 | 실제 존재
　| 고유성

### 2. 추상화

위의 내용에 따라 클래스의 공통의 속성이나 기능을 묶어 이름을 붙이는 것을 자료의 추상화라고 한다.  
이해를 돕기위한 예시 :

![explain_image1](https://user-images.githubusercontent.com/45117394/49082783-fe909980-f28d-11e8-8f30-a47050b99aed.jpg)
      
### 3. 캡슐화 (Encapsulation)

이렇듯 객체를 하나의 부품 이라고 가정한다면, 객체를 만드는 과정은 좋은 부품을 만드는 과정이라고 생각하면 된다.  
하나의 부품(객체)과 케이스(함수)를 만든다면 이들을 클래스라고 정의해줄 수 있으며, 이 과정을 '캡슐화' 라고 말할 수 있다.

#### 3-1) 인스턴스 변수와 특징
```
  class C:                      # C라는 클래스를 생성한다.
    def __init__(self, v):      # 생성자 __init__ 초기화
        self.value = v
    def show(self):
        print(self:value)
  c1 = C(10)                    # 인스턴스를 가르킬 c1
  print(c1.value)               # 인스턴스 c1의 value의 값을 출력한다.
  c1.value = 20
  print(c1.value)
  c1.show()
  
```
> **Result**  
> 10  
> 20
#### 3-2) set/get 메소드

```
  class C:                      
    def __init__(self, v):      
        self.value = v
    def show(self):
        print(self:value)
    def getValue(self):
        return self.value
    def setValue(self, v):      # 입력값
        self.value = v
  c1 = C(10)                    
  print(c1.getValue())          
  c1.setValue(20)
  print(c1.getValue())
  
```
> **Result**  
> 10  
> 20

#### 3-2) 왜 set/get 메소드를 사용해야 하나?

파이썬의 경우 인스턴스 변수에 직접 접근이 가능하지만 아래와 같은 사례로 인해 오류가 날 수 있다.  
만약 누군가가 v1의 값에 'one'이라는 문자열 데이터를 넣었을 때, 프로그램이 과연 이해할 것인가?  
그리고 정해진 v1의 값에 누군가가 다시 바꾸는 과정을 못하게 막을 것인가?  
이런 단순한 문제부터 이해하고 코딩한다면 차후 복잡한 로직(조건문, 반복문 등)을 개발하는데 도움이 될 것이다.  
(이해가 안 갈 수도 있다. 따라서 자세한 사항은 다음 챕터에서 확인해보자)  

```
  class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):     # v1 값이 정수형인지 검증 과정
            self.v1 = v1
        if isinstance(v2, int):     # v2 값이 정수형인지 검증 과정
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):      # 만약 v가 숫자라면 :
            self.v1 = v
    def getV1(self):
        return self.v1
  c1 = Cal(10,10)
  print(c1.add())
  print(c1.subtract())
  c1.setV1('one')
  c1.v2 = 30
  print(c1.add())
  print(c1.subtract())
  
```
> **Result**  
> 20  
> 0  
> 40  
> -20

나도 솔직히 무슨말인지 모르겠으니, 밑에 속성으로 내려가보자.

#### 3-3) 속성(Property)

자바와 같은 객체 지향 언어에서는 외부로부터 바로 접근할 수 없는 prviate 객체 속성을 지원합니다.  
이러한 언어에서는 ```private``` 속성의 값을 읽고(get) 변경(set)하기 위해 getter 메서드와 setter 메서드를 사용합니다.  
하지만, 파이썬에는 ```getter``` 메서드나 ```setter```메서드가 없습니다.  
파이썬에서 선언되는 모든 속성(변수)와 메서드는 public이기 때문입니다.  
파이썬에서는 사용자가 속성에 직접 접근을 막기 위해 ```getter``` 또는 ```setter``` 메서드 대신에 프로퍼티(property) 를 사용합니다.  
> 참고 : 변수명에 홑밑줄(_)과 겹밑줄(__)이 있습니다.
>> * 홑밑줄(single underscore) : 보통 내부적으로 사용하는 변수일 때 사용합니다.
>> * 곁밑줄(double underscore) : 클래스 외부에서 접근할 수 없도록 내부 변수로 만듭니다.

```
  class Cal(object):
  
  class University:
    def __init__(self, university_name):
        self.__university_name = university_name
 
    @property
    def university_name(self):                      # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋다. 
        return self.__university_name
 
    @university_name.setter                         # @는 데커레이터(decorator)라고 하는데, 말그대로 뭔가를 꾸며주는 함수를 의미한다.
                                                    # 같은 university_name 메서드이지만 장식자 @ 에 의해 서로 다른 역할을 한다.
    def university_name(self, new_university_name): # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋다. 
        # 대학교 이름을 변경하는 setter 메서드
        self.__university_name = new_university_name
        print("============ setter를 통해 대학교 이름을 변경합니다============")
        print('변경 후 대학 이름 : {} '.format(self.university_name))
        
    university = University('조선대학교')
    print(university.university_name)
    university.university_name = '전남대학교'        # 객체의 속성값에 직접 접근하는듯이 사용하지만 
                                                    # 실제로는 메서드 호출을 통해 변수에 접근한다. 
    print(university_university_name)
  
```
> **Result**
>> 조선대학교  
>> ============ setter를 통해 대학교 이름을 변경합니다============  
>> 변경 후 대학 이름 : 전남대학교 

만약 프로퍼티(property)가 없었다면 대학교 이름을 아래처럼 불편하게 수정해야 했을지도 모른다.  
```property```를 이용하면 클래스의 정의에 있는 코드만 수정하면 손쉽게 속성을 변경 할 수 있다.

```
  기존코드
  > university = University('조선대학교')
  > university = University('전남대학교')
  
  개선된 코드
  > university = University('조선대학교') 
  > university.university_name = '전남대학교'
```
만약 ```setter``` 프로퍼티를 명시하지 않으면 읽기전용(```read-only```)이 되어 외부에서 값을 변경할 수 없습니다.  
```setter``` 프로퍼티를 주석처리하면 ```can't set attribute```의 출력결과를 얻습니다.  

어렵다면 일단 넘어가자.

### 4. 상속(Inheritance)
#### 4-1) 상속의 개념
상속이란? 자신이나 타인이 만들어 놓은 객체에 새로운 기능을 추가해서 새로운 객체를 만들어 내는 행위이다.  
쉽게 말해, 기능을 상속해서 새로운 기능을 만든다.  
그렇다면 왜 상속이 필요한가? 에 답은 불필요한 반복을 줄이기 위함이고 이는 유지보수의 편의성을 제공한다.  

```
  class Class1(object):
      def method1(self): return 'm1'
  c1 = Class1()
  print(c1, c1.method1())               # c1, 어떤 값에 대한 결과인지 확인이 어려우니 
                                        # 대응하는 클래스가 무엇인지를 출력하라는 뜻이다.
  class Class3(Class1):                 # Class3가 Class1을 상속 받는다.
      def method2(self): return 'm2'    # Class3가 Class1의 기능을 가짐과 동시에 method2를 추가했다.
  c3 = Class3()
  print(c3, c3.method1())
  print(c3, c3.method2())

  class Class2(object):
      def method1(self): return 'm1'
      def method2(self): return 'm2'
  c2 = Class2()
  print(c2, c2.method1())
  print(c2, c2.method2())
  
```
> **Result**
>> <__main__.Class1 object at 0xb757dfec> m1  
>> <__main__.Class3 object at 0xb758704c> m1  
>> <__main__.Class3 object at 0xb758704c> m2  
>> <__main__.Class2 object at 0xb758708c> m1  
>> <__main__.Class2 object at 0xb758708c> m2  

복잡하고 어렵쥬? 이해하는데 오래걸릴거 같아 보여유

#### 4-2) 상속(Inheritance) 응용

기존의 계산기 프로그램에 ([참고] 생활코딩)을 상속을 활용하여 곱하기와 나누기 기능을 추가&수정 해봅시다.

```
  class Cal(object):
      def __init__(self, v1, v2):
          if isinstance(v1, int):
              self.v1 = v1
          if isinstance(v2, int):
              self.v2 = v2
      def add(self):
          return self.v1+self.v2
      def subtract(self):
          return self.v1-self.v2
      def setV1(self, v):
          if isinstance(v, int):
              self.v1 = v
      def getV1(self):
          return self.v1
  class CalMultiply(Cal):              # 곱하기
      def multiply(self):
          return self.v1*self.v2
  class CalDivide(CalMultiply):        # 나누기
      def divide(self):
          return self.v1/self.v2
  c1 = CalMultiply(10,10)             
  print(c1.add())
  print(c1.multiply())
  c2 = CalDivide(20,10)
  print(c2, c2.add())
  print(c2, c2.multiply())
  print(c2, c2.divide())

```
> **Result**  
>> 20  
>> 100  
>> <__main__.CalDivide object at 0x000000000316CDA0> 30  
>> <__main__.CalDivide object at 0x000000000316CDA0> 200  
>> <__main__.CalDivide object at 0x000000000316CDA0> 2.0

상속이라는 것은 메소드만을 상속하는 것이 아니고 그 부모 객체가 가지고 있는 변수도 상속받는다.  

## 파이썬 클래스 멤버
#### 4-1) 클래스 멤버와 인스턴스 멤버의 차이의 이해

http://pythonstudy.xyz/python/article/19-%ED%81%B4%EB%9E%98%EC%8A%A4  
존나 설명 잘됨

# 먼 개소리인지 하나도 이해 안되~~~
![d0e959371d21e7682b4460c9544ef36d_pulling-hair-out-quotes-pulling-hair-out-of-head-clipart_2700-1962-1440x1046](https://user-images.githubusercontent.com/45117394/49106040-6dd5b000-f2c5-11e8-9783-fcab9f4170ff.jpeg)

---- 생활코딩 새벽 4시 22분 ---- 멘탈 터짐 ㅂ2 

## 파이썬 Override
