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
 
 ## 객체와 변수 (편집중 by 이주환)
