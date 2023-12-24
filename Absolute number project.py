#Absolute number project.
def absolute_value(x):
    """
    This function will check if a number is positive or not and return its absolute value. Let's x the real number, if x is smaller than 0 then 
    its absolute value will be -x, but if x is greater than or equal to 0 then its absolute value will be the x itself.
    """
    if x<0:
        return -x
    else:
        return x
