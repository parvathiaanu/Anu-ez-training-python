#abstarct program
"""

from abc import ABC,abstractmethod
class abstarctdemo(ABC):
    @abstractmethod  #called decoration used for making  abstract 
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class demo(abstarctdemo):#making abstarct concrete
    def display(self):
        print("abstaction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()


#inheitance
#single

class parent:
    def display(self):
        print("parent class")
class child (parent):
    def show (self):
        print("child class")
c=child()
c.display()
c.show()

class a():
    n=30
class b(a):
    def calc(self):
        c=self.n+70
        print(c)
obj=b()
obj.calc()


#MUTIPLE INHERITANCE


class mom:
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
       print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()

#multi-level inheritance


class grandparent:
    def display(self):
        print("grandparent class")
class parent (grandparent):
    def show(self):
        print("parent class")
class child (parent) :
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing()

#heirarchial

class parent:
    def display(self):
        print("parnent class")
class child1 (parent):
    def c1display(self):
        print("child1 class")
class child2 (parent):
    def c2display(self):
        print("child2 class")

c1=child1()
c1.display()
c1.c1display()
#c2.c2display()
c2=child2()
c2.display()
#c2.c1display()
c2.c2display()
"""

#hybrid


class parent:
    def display(self):
        print("parent class")
class  child1 (parent):
    def child1display(self):
        print("child1 class")
class child2(parent):
    def child2display(self):
        print("child2 class")
class kid1(child1):
    def kid1display(self):
        print("kid1 class")
class kid2(child1):
    def kid2display(self):
        print("kid2 class")
class kidd1(child2):
    def kidd1display(self):
        print("kidd1 class")
class kidd2(child2):
    def kidd2display(self):
        print("kidd2 class")
k1=kid1()
k1.display()
k1.child1display()
k1.kid1display()
k2=kid2()
k2.display()
k2.child1display()
k2.kid2display()
kd1=kidd1()
kd1.display()
kd1.child2display()
kd1.kidd1display()
kd2=kidd2()
kd2.display()
kd2.child2display()
kd2.kidd2display()











        




































































