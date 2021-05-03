fibonacci=[]
num1=1
num2=1
num3=0

while num1<=55:
  fibonacci.append(num1)
  num3=num1+num2
  num1=num2
  num2=num3
print(fibonacci)
