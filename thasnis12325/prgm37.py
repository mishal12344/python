class Publisher:
    def __init__(self,name1):
      self.name=name1
    def show(self):
        pass
class Book(Publisher):
    def __init__(self,title1,author1,name1):
        self.title=title1
        self.author=author1
        Publisher.__init__(self,name1)
    def show(self):
        pass
class Python(Book):
    def __init__(self,p,no,title1,author1,name1):
        self.price=p
        self.no__of__page=no
        Book.__init__(self,title1,author1,name1)
    def show(self):
        print('Book title:',self.title)
        print('Author:',self.author)
        print('publisher:',self.name)
        print('price:RS.',self.price)
        print('No of pages:',self.no__of__page)
P1=Python(700,300,'programming with python','GV Rossum','ABC Books')
P1.show()

