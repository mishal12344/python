class student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno

  def printname(self):
    print(self.name, self.rollno)
x = student("thasni", "57")
x.printname()
