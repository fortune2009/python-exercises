#calculating the angles in the triangle
#chapter 1 no. 29

#note that the cos inverse is yet to be resolved

import math

a = 3
b = 7
c = 9
# c2 = a2 + b2 - 2*a*b*c*Cos C
A = math.cos((b**2 + c**2 - a**2)/(2*b*c))
B = math.cos((a**2 + c**2 - b**2)/(2*a*c))
C = math.cos((b**2 + a**2 - c**2)/(2*b*a))

print("Angles A= {}, B= {}, C= {}".format(A,B,C))
