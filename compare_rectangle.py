class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare_area(self, other):
        if self.area() > other.area():
            return "The first rectangle has a larger area."
        elif self.area() < other.area():
            return "The second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."

length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))

length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))

rect1 = Rectangle(length1, breadth1)
rect2 = Rectangle(length2, breadth2)

print(f"Area of the first rectangle: {rect1.area()} square units")
print(f"Perimeter of the first rectangle: {rect1.perimeter()} units")
print(f"Area of the second rectangle: {rect2.area()} square units")
print(f"Perimeter of the second rectangle: {rect2.perimeter()} units")

comparison_result = rect1.compare_area(rect2)
print(comparison_result)
