import random 
print('welcome to guessing game')
print('who will guess the number')
print('1. You will guess the number \n 2. Computer will guess the number' )
choice = int(input('Enter your choice: '))
if choice ==1:
    secret= random.randint(1, 100)
    attempts = 0
    while True:
        guess= int(input('Guess the number from 1 to 100: '))
        attempts = attempts+1
        if guess > secret:
            print('number is too high')
        elif guess < secret:
            print('number is too small')
        else:
            print('found number: ', attempts, 'attempts')
            break
elif choice ==2:
    low= 1
    high= 100
    attempts = 0
    while True:
        guess= random.randint(low, high)
        print('computer guess: ', guess)
        attempts = attempts+1
        user_input= input('is the number correct? (yes/no) ')
        if user_input.lower() == 'yes':
            print('computer found the number in ', attempts, 'attempts')
            break
        elif user_input.lower() == 'no':
            user_input= input('is the number higher or lower? (higher/lower) ')
            if user_input.lower() == 'higher':
                low = guess + 1
            elif user_input.lower() == 'lower':
                high = guess - 1
else:
    print('invalid choice')