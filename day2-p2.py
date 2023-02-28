
    #encapsulation
#protected     
class encap:
    __a=10
    c=20
    def enacapfunction(self):
        __b=200
        print("encap function -accesing protected")
        #print(self.__a+10)#throws an error 
obj=encap()
#print(obj.__a)
obj.enacapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        #print(self.__a)
obj=encap()
obj.encapfunction()
#print(obj.__a)

#method over-loading
class moverload :
    def display(self,a=None,b=None):
       print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with all arguments:")
obj.display(20,30)
print("with single value:")
obj.display(10)

   #polymorphism

class vijayawada():
    def placename(self):
        print("kulu")
    def student(self):
        print("yes")
    def whichyear(self):
        print("3rd year")
class hyd():
    def placename(self):
        print("hyd-kulu")
    def student(self):
        print("yes-hyd")
    def whichyear(self):
        print("3rd year-hyd")
objvyw=vijayawada()
objhyd=hyd()
for details in (objvyw,objhyd):
    details.placename()
    details.student()
    details.whichyear()


#creating node declaration and definition
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
       self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#tempfirst node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next

obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
       self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#tempfirst node
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next

obj=singlelinkedlist()
n=node('W')
obj.head=n
n1=node('I')
obj.head.next=n1
n2=node('N')
n1.next=n2
n3=node('N')
n2.next=n3
n4=node('E')
n3.next=n4
n5=node('R')
n4.next=n5
obj.display()


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __int__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
print("before inserting 100")
obj.display()
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print("before inserting 555")
obj.display()
print("after inserting 555")
obj.insert_beginning(555)
obj.display()

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __int__(self):
        self.head=None
    def insert_end (self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
print("before inserting 100")
obj.display()
print("after inserting 100")
obj.insert_end (100)
obj.display()
print("before inserting 555")
obj.display()
print("after inserting 555")
obj.insert_end (555)
obj.display()

#position insert
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __int__(self):
        self.head=None
    def insert_position (self, pos,data):
        np=node(data)
        for i in range(pos-1):
           temp=self.head
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
print("before inserting 100")
obj.display()
print("after inserting 100")
obj.insert_position (4,100)
obj.display()
print("before inserting 555")
obj.display()
print("after inserting 555")
obj.insert_position (2,555)
obj.display()

#user input single linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current= self.head
        while current is not None:
            print(current.data,end="")
            current=current.next
a_llist=linkedlist()
n=int(input())
for i in range(n):
    data =int(input("enter"))
    a_llist.append(data)
print("the linked list",end="")
a_llist.display()




    
















































            
    



































