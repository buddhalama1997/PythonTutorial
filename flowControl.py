# This a program for possible case in the rainy season

# Greeting and asking their name
print('Hello! Enter Your Name')
# input name from keyboard
name=input()

# Asking a question
print( name +', Is it raining outside? Please enter Y for yes and N for NO')

# input answer from the keyboard
answer = input()
# checks the answer and gives the suggestion
if answer == 'N':
    print ('Go Outside')
# If above statement in not satisfied then else statement will execute.
else:
    print('Have you Umbrella? Please enter Y for yes and N for NO')
    answer = input()
    if answer == "Y":
        print('Go Outside')
    else:
        print('Wait for while')
        print('Is it raining outside? Please enter Y for yes and N for NO ')
        answer = input()
        if answer =='N':
            print ('Go Outside')
        else:
            while answer == 'Y':
                print('Wait for while')
                print('Is it raining outside? Please enter Y for yes and N for NO ')
                answer = input() 
