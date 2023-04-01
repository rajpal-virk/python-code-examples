'''
Write a function to add 2 numbers

author : Rajpal Virk
'''

__author__ = "Rajpal Virk"
__email__ = "rajpal.virk@outlook.com"
__status__ = "Training"

def sum2num(x,y):
    if type(x) and type(y) not in [int, float]:
        raise TypeError('Input value types can only be integer or float')
    return(x+y)




