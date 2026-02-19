class Room:
    roomBuild = "peter hostel"

    def __init__(self):
        self.no = 20
        self.name = "pvt"

    def renew(self, no, name):
        print(self.no)
        print(self.name)

    @classmethod
    def roombuilding(cls):
       cls.roomBuild = "mathew"
       print(cls.roomBuild)


    @staticmethod
    def hostel():
        print("gyuy")


floor1 = Room()

floor1.renew(45,"fgfh")
floor1.roombuilding()
floor1.hostel() 


#simple inheritance

class college:
    def name(self):
        print("name23")
class department(college): #single
    def coordinator(self):
        print(coordinator)
dep=department()
dep.name()

#multiple inheritance
class college:
    def name(self):
        print("name23")
class department:
    def coordinator(self):
        print("coordinator")
class sec(college,department): #multiple
    def section(self):
        print("a section")
obj1=sec()
obj1.name()

#multilevel
class college:
    def name(self):
        print("name23")
class department(college):# multilevel
    def coordinator(self):
        print("coordinator")
class sec(department):  #multilevel
    def section(self):
        print("a section")
obj1=sec()
obj1.coordinator()

#hierarchical

class college:
    def name(self):
        print("name23")
class department(college):# hierarchical
    def coordinator(self):
        print("coordinator")
class sec(college): # hierarchical
    def section(self):
        print("a section")
obj1=sec()
obj1.section()

#hybrid collection of any two inheritance  


#super keyword
class rain:
    def __init__(self):
        print("raining")
class sun(rain):
    def __init__(self):
        super().__init__()
        print("sunny")
        
class winter(sun):
    def __init__(self):
       super().__init__()
       print("cool")
obj=sun()

#polymorphism

class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class bird(animal):
    def sound(self):
        print("birds sing")
obj1=dog()
obj1.sound()

#example
class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self,c,d):
        print(c*d)
sha=shape()
print(sha.area())
a=int(input())
b=int(input())
rec=rectangle()

rec.area(a,b)


class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,grade):
        self.grade=grade
        
    def display(self,name,grade):
        super().__init__(name)
        print(self.name)
        print(self.grade)
        
s1=student("a")
s1.display("aaa","a")

class employee:
    def __init__(self,name,salary):
      self.name=name
      self.salary=salary
class manager(employee):
    def __init__(self,department):
      self.department=department
      print(department)
    def display(self,name,salary):
        super().__init__(name,salary)
        print(name)
        print(salary)
        
m1=manager("eee")
m1.display("sss",344)

#encapsulation (public ,private, protected)

class childname:
    def __init__(self):
        self.__childname="athithi"
    def findchildname(self):
        print(self.__childname)
class grandchild(childname):
    pass
c1=childname()
c1.findchildname()

#exception handling
try:
    a=int(input())
except Exception as e:
    print(Exception,e)

try:
    a=int(input()) #value error
    b=int(input())
    c=input()
    d=a/c #type error
    print(e) #name error
except ValueError as e:
    print(ValueError,e)

except TypeError as e:
    print(TypeError,e)

except NameError as f:
    print(NameError,f)
finally:
    print("done")











    

