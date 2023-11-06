class rect:
    def __init__(self,l,b):
      self.a1=1
      self.a2=b
    def area(self):
        self.m=self.a1*self.a2
    def peri(self):
         self.n=2*(self.a1*self.a2)
    def disp(self):
        print("area of rectangle:",self.m)
        print("perimeter of retangle:",self.n)
    def compare(self,obj2):
        if self.m==obj2.m:
           print("area are equal")
        elif self.m>obj2.m:
            print("area 1 is greater than area2")
        else:
           print("area2 is grater than area1")
l1=int(input("enter the length 1:"))
b1=int(input("enter the breadth 1:"))
l2=int(input("enter the length 2:"))
b2=int (input("enter the breadth2:"))
obj1=rect(11,b1)
obj2=rect(12,b2)
obj1.area()
obj1.peri()
obj2.area()
obj2.peri()
obj1.disp()
obj2.disp()
obj1.compare(obj2)
