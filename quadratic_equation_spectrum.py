import math
a = int(input("enter the first coefficient"))
b = int(input("enter the second coefficient"))
c = int(input("enter the third coefficient"))

d = ((b * b) - (4 * a * c))
if d == 0:
	print("the roots are equal")
	print("the root is ", s )
elif d > 0:
	x1 = (-b + math.sqrt(d)) / (2 * a)
	x2 = (-b - math.sqrt(d)) / (2 * a)
	print("two roots are : ", x1, x2)
else:
	print("roots are imaginary")
	exit()


