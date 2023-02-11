# -*- coding: utf-8 -*-
"""
Assignment Description: Assignment for Rongda Kang this a edited version of original file 
for testing and it is design to classify triangle
@author: Rongda Kang
Summary: The primary goal of this file is to demonstrate a simple python program and learn
How to wirte the unittest in away is well formated
I am here to Pledge that all of the assignment is done by myself
Detail: I mad a lot of changes
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';

    # require that the input values be >= 0 and <= 200
    elif a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    elif a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
        
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and c == a:
        return 'Equilateral'
    elif((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((b**2 + c**2) == a**2):
        return 'Right'
    elif (a != b) and (b != c) and (c!=a):
        return 'Scalene'
    else:
        return 'Isoceles'
