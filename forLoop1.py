# for loop to print the value from 12 to 16
# it will return 12, 13, 14,15. It doesn't print the end value
for i in range(12,16):
    print (i)

print('Next For loop')

# assigning total variable
total = 0
# For loop to calculate the first 10 numbers i.e 0,1,2,3,4,5,6,7,8,9
for i in range (10):
    total = total + i
print(total)

print(" Next For Loop")

# first two argument is start argument and stop argument.
# Whereas third argument is step argument
# In each iteration value of variable is increased by step argument value (i.e 2 in our case)
for i in range (0,10,2):
    print(i)


print('Next For Loop')
# In each iteration value of variable is descresed by step argument value(i.e. -2 in our case)
for i in range (5,-1,-2):
    print(i)