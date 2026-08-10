n= int(input('enter a value:'))
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if temp==sum:   
       print('its a palindrome ')
else:
    print('its a not palindrome ')       