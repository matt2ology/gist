#########################
# RULES: Variable Scope #
#########################
"""
1) Global Scope
What variables your functions are allowed to use:
If the variable is created outside the function and above it
your function can access that variable.
"""
a = 42


def butter():
    print("\tIn function Butter")
    """
    2) Variable 'b' is local to function butter and can't be
    accessed outside of the function.
    """
    b = "corn"
    print(a)
    print(b)


c = "Nuggets"


def fudge():
    print("\tIn function fudge")
    print(a)
    print(c)


butter()
fudge()
