"""
########################################################
# Argument for having a default argument in a function #
########################################################
Say that we are using Python for web development and we're
making a social network and whenever the user signs up they
can select if they are male or female, then it will display
on their profile; however, if they entered nothing then we
don't want to enter an empty value into our database or else
bad things can happen or get some unexpected results, so we
want to set a default value (like unlisted).
"""


def get_gender(sex="Unknown"):
    if sex is 'm' or sex is 'M':
        sex = "Male"
    elif sex is 'f' or sex is 'F':
        sex = "Female"
    print(sex)


get_gender('M')
get_gender('F')
get_gender('m')
get_gender('f')
get_gender()

