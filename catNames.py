# Assigning empty list
catNames = []

# While loop until the statement is false
while True:

    # prompt message for direction
    print("Enter the name of cat or Enter nothing to exit.")
    
    # taking input from the keyboard
    name = input()

    # If there is nothing input from the keyboard
    if name == '':
        break
    # Append the list
    catNames = catNames + [name]

print('The name of cats are:')

# to print the all values in list
for i in catNames:
    print( '    '+ i)