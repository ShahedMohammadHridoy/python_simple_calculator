from math import sqrt

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

if (a+b)>c and (b+c)>b and (c+a)>a:
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)
else:
    print("Triangle not possible.")