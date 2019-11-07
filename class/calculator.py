class Calculator: 
 def addition(self,first,second):
	  return first+second
 def multiplication(self,first,second):
	  return first*second
 def subscription(self,first,second):
      return first-second
 def division(self,first,second):
      return second/first
 def remindring(self,first,second):
      return second%first
first=30
second=60 
obj=Calculator()
print("Addition of two Number=%d\n"%(obj.addition(first,second))) 
print("multiplication of two Number=%d\n"%(obj.multiplication(first,second))) 
print("subscription of two Number=%d\n"%(obj.subscription(first,second))) 
print("division of two Number=%d\n"%(obj.division(first,second))) 
print("remindring of two Number=%d\n"%(obj.remindring(first,second))) 
 