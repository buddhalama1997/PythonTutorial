# defining fuctio for collatz
def collatz(num):
    # itteration till num = 1
    while (num !=1):
        # check the condition if remainder is zero
        if num % 2 == 0:
            num = num//2
            print(num)
            continue
        # check the condition if remainder is not zero
        elif num%2 ==1: 
            num= num*3 +1
            print(num)
            continue
        # if number is 1 it return 1
        else:
            print(num)
            break

# tiggering collatz function
collatz(3)