'''This is the docstring describing this module for calculating friends' expenses.'''

def food(f,num):
    tip=0.1*f
    f=f+tip
    return f/num

def movie(t,num):
    return t/num
print("the name attribute is ",__name__)
