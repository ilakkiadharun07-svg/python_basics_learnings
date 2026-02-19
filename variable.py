a=input("enter name")
b=int(input("enter age"))
print("my name is ",a)
print("my age is ",b)

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
mul=a*b*c
add=a+b+c
div=mul/add
print( div)

score=int(input())
a=score/10
print(a,"/10")

if(False):
    print("yes")
else:
    print("no")

meghna=input()
if(meghna=="died"):
    print("surya meets priya")
else:
    print("surya weds meghna")

num=int(input())
a=num%3
b=num%5
if(a&b==0):
    print("divisible")
else:
    print("not")

num=int(input())
a=num%2
if(a==0):
    print("even")
else:
    print("odd")

score=int(input())



name=input()
dep=input()
if(score>70):
    print("eligible")
else:
    print("not")

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
avg =(a+b+c+d+e)/5
if(avg<35):
    print("additional class")
else:
    print("good")


a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)

for i in range(1,11):
    if (i%2==0):
        print(i)

count1=0
count2=0
for i in range(1,11):
    if (i%2==0):
        count1+=1
        
    else:
        count2+=1
        

print("Total Even:", count1)
print("Total Odd:", count2)  




count=0
for i in range(1,101):
    if (i%3==0 and= i%5==0):
        count+=1
print(count)



b=[]
for i in range(5):
    a=int(input("enter name"+str(i)))
    c=b.append(a)
print(b)

sum=0
for i in b:
    sum+=i
print("sum",sum)

n=int(input("enter number"))
for i in range(1,n+1):
       print(str(i))

a=int(input("enter num"))
for i in range(1,a+1):
      print("number is",i,"and cube of the",i,"is:",i*i*i)


for i in range(1,6):
    print("week:",i)
    for j in range(1,8):
       print("day:",j)

for i in range(1,5):
    print()
    for j in range(1,i+1):
      print("*",end="")

i=10
while(i<=10 and i>=0):
    print(i)
    i=i-1

i=6
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)


"""     duplicates     ordered    add and modify  changeable
list - yes   yes yes yes
tuple-yes yes no no
sets-no(removed) no (not modify can add) no
dictionaries-no yes yes yes """

a=int(input())
b=int(input())
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
add()
sub()
mul()
div()

def my_range(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input())
b=int(input())
my_range(a,b)


user="emc"
password="123"
u_name=input()
pass_word=input()
def validate():
    if(user==u_name and password==pass_word):
        print("True")
    else:
        print("false")
validate()

def add(s1,s2):
    return s1+s2
a=int(input())
b=int(input())
c=int(input())
sum=add(a,b)
d=sum*c
print(d)


class love:
    date=""
    gift=""
    def marriage():
        print("love marriage")
    def divorce():
        print("arrange marriage")
appa=love()
amma=love()
appa.marriage="goood"
print(appa.marriage)
appa.gift="yes"
amma.gift="no"
print("appa",appa.gift)
print(amma.gift)


class mobile:
    def __init__(self):
        
        self.model="uuu"
        self.color="aaa"
    def details(self):
        print("model",self.model)
        print("color",self.color)
oppo=mobile()
samsung=mobile()
#oppo.model="a3i"
#oppo.color="red"
#samsung.color="white"
#samsung.model="galaxy"
oppo.details()
samsung.details()

class student:
    def __init__(self):
        self.name="a"
        self.reg_num="b"
    def display(self):
        print(self.name)
        print(self.reg_num)
student1=student()
student1.display()

class job:
    def __init__(self,role,salary):
        self.role=role
        self.salary=salary
    def display(self):
        print("role",self.role)
        print("salary",self.salary)
fresher = job("software","6 lpa")
fresher.display()





class Room:
    roomBuild = "peter hostel"

    def __init__(self):
        self.no = 20
        self.name = "pvt"

    def renew(self, no, name):
        self.no = no
        self.name = name
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

floor1.renew(101, "John")
floor1.roombuilding()
floor1.hostel()
