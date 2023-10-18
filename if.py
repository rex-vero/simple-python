print('first number: ')
num1=int(input())
print('second number: ')
num2=int(input())
print('+ or - or * or ** or / or %')
operator = str(input())
if operator=="+":
     print('result: ',num1+num2)
elif operator=="-":
    print('result: ',num1-num2)
elif operator=="*":
    print('result: ',num1*num2)
elif operator=="**":
    print('result: ',num1**num2)
elif operator=="/":
    print('result: ',num1/num2)
elif operator=="%":
     print('result: ',num1%num2)
else:
     print('error') 
    
