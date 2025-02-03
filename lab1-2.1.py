import sys
import math
def do_stuff():                     
    a = float(sys.argv[1])
    b = float(sys.argv[2])                                     #the purpose of this code is to find the roots of a quadratic equation
    c = float(sys.argv[3])                                     #the error in the code was the use of incorrect quotes, and also not adding an if statement to check whether a is 0
    if a == 0:                                                 #because a cannot be equal to 0 in a quadratic equation
        print("Error: 'a' cannot be zero in a quadratic equation.")
        return                                                            
    d = b**2 - 4*a*c                                            
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')               
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')
do_stuff()