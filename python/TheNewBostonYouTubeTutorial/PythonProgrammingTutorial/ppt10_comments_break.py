#################
# Concatenation #
#################
'''
# CAN NOT ADD A STRING AND MATH NUMBER TO CONCATENATE 
print("Matt" + 2)
# To concatenate strings and numbers use a comma
print("Matt", 2)
'''

#####################################
# This program finds a magic number #
#####################################
'''
magicNumber = 26
# In the range of 101 (numbers 0 - 101)
for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number!")
        
        # When you have a break it 'breaks' out of the 
        # loop completely and stops the entire loop
        break
    # Print every number leading up to the magic number(0, 1, 2, ..)
    else:
        print(n)
'''
##################################################################
# Bucky's homework                                               #
##################################################################
# Have a program to loop through the numbers 1 - 100 and print   #
# out all numbers that are multiples of four (4, 8, 12, 16, ...) #
##################################################################
for number in range(1, 101):
    if number%4 is 0:
        print(number)
