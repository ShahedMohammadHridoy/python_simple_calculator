import math
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
d = b**2-4*a*c
if d==0:
    x = b+2*a
    print("The roots are real and equal",x,x)
elif d>0:
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("The roots are real and unequal:", x1, x2)
else:
    print("Roots are immiginary.")
