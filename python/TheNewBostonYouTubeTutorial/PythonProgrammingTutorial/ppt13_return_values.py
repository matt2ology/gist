###################
# Define function #
###################
def allowed_dating_age(my_age):
    girls_age = (my_age/2) + 7
    return girls_age

##################################################
# Assigning a return type function to a variable #
##################################################
limit = allowed_dating_age(31)

print("I can date girls", limit, "or older.")

###############################################################
# Bucky's homework                                            #
###############################################################
# Go through a list of ages of 15 to 60 and print the dude's  #
# age and and their limit next to each other.                 #
###############################################################

for age in range(15, 60+1):
    limit = allowed_dating_age(age)
    print("A", age, "year old can date a", limit, "or older.")
