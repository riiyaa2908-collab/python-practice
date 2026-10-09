a = int(input('enter first number: '))
b= int(input('enter second number: '))
print('enter two numbers', a, b)
print('choose method: \n 1.addition \n 2.subtaction\n 3.multipilication \n 4.division\n 5.square')
n= input('enter your choice: ')
choices = n.split(',')
for choice in choices:
    choice= int(choice)
    if  choice==1:
        sum= a+b
        print(f"1.addition: {sum}")
    elif choice==2:
        sub= a-b
        print(f"2.Subtraction: {sub}")
    elif choice==3:
        mul= a*b
        print(f"3.Multiplication: {mul}")
    elif choice==4:
        div= a/b
        if b == 0:
            print('invalid operation')
        else:
            print(f"4.Division: {div}")
    elif choice==5:
        sqa= a**2
        sqb= b**2
        print(f"5.Square: for a = {sqa}\n for b = {sqb}")
    else:
        print('invalid choice')
        