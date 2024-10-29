a=0
b=1
n=int(input("Enter a Number for Fabonacchi-Series "))
if n<=0:
  print("Please enter a positive number")
elif n==1:
  print("Fibonacci Series is : ",a)  
else:
 for i in range(n):
  print("Fibonacci Series is : ",a)  
  next=a+b
  a=b
  b=next
  


