from circle import circlearea
from circle import circleperi
from rectangle import rectarea
from rectangle import rectperi
#from 3Dgraphics.cuboid import cuboidarea
#from 3Dgraphics.cuboid import cuboidperi
#from 3Dgraphics.sphere import spherearea
#from 3Dgraphics.sphere import sphereperi


l=int(input("enter the length of rectagle :"))
b=int(input("enter the breadth of rectangle :"))
print("area of rectangle is :",rectarea(l,b))
print("perimeter of rectangle is :",rectperi(l,b))

r=int(input("Enter the radius of circle :"))
print("area of circle is :",circlearea(r))
print("perimiter of circle is :",circleperi(r))

r=int(input("Enter the radius of sphere :"))
print("area of sphere is :",spherearea(r))
print("perimiter of sphere is :",sphereperi(r))


l=int(input("enter the length of cuboid :"))
w=int(input("enter the width of cuboid :"))
h=int(input("enter the height of cuboid :"))
print("area of rectangle is :",cuboidarea(l,h,w))
print("perimeter of rectangle is :",cuboidperi(l,w,h))
