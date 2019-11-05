sum=0
number = 153
rem=None
tmp=number
i=1
while number >=1 :
    rem=number%10
    rem=rem*rem*rem
    sum=sum+rem
    number=number/10
if tmp == sum :
    print("True=%d"%sum)
else:
    print("Flase=%d"%sum)