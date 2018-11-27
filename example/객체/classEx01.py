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


#Cal클래스에 값을 넣고 변수에 저장
	
c1 = Cal(10, 10)

print(c1.add()) #더하기
print(c1.subtract()) #빼기

c2 = Cal(30, 20)

print(c2.add())
print(c2.subtract())