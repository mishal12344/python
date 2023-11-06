class rectangle:
    def __init__(self,l,b):
        self.__l1=l
        self.__b1=b
    def area(self):
        area1=self.__l1*self.__b1
        return area1
    def __lt__(self,obj):
        if (self.area()<obj.area()):
          return "the area of rectangle1 is less than rectangle2"
        else:
          return "the area of rectangle2 is less than rectangle1"
print("rectangle 1")
l=int(input("enter the length of rectangle1:"))
b=int(input("enter the breadth of rectangle1:"))
obj1=rectangle(l,b)
print("the area is:")
print(obj1.area())
print("rectangle 2")
l=int(input("enter the area of retangle2:"))
b=int(input("enter the breadth of rectangle2:"))
obj2=rectangle(l,b)
print("the area is:")
print(obj2.area())
print("now comparing the rectangles")
print(obj1<obj2)


