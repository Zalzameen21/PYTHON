class Rectangle:
    def _init_(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))

length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))

rect1 = (length1, breadth1)
rect2 = (length2, breadth2)

if rect1.area()>rect2.area():
    print("1 is gtrt area",rect1.area(),"perimtr",rect1.perimeter())
elif rect1.area()<rect2.area():
    print("2 is grtr area",rect2.area(),"perimtr is",rect2.perimeter())
    
else:
    print("both are equal rect one is",rect1.area(),rect1.perimeter(),"rect 2 is",rect2.area(),rect2.perimeter())
