num= int(input("Enter a number: "))
div= int(input("Enter the divisor: "))
start_range= int(input("Enter the starting range: "))
end_range= int(input("Enter the ending range: "))
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:
    print("The number is zero.")

if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

if num%div==0:
    print("The number is divisible by ", div, )                    
else:
    print("The number is not divisible by ", div, )
if (num>=start_range) and (num<=end_range):
    print("The number is in the range of ", start_range, " and ", end_range)
else:
    print("The number is not in the range of ", start_range, " and ", end_range)            