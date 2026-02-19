#incresing pattern
n = int(input("Enter rows: "))

for i in range(n):
    for j in range(i + 1):
        if(i%2==0):
            print("0", end=" ")
        else:
            print("1",end=" ")
    print()


#increasing pattern
n = int(input("Enter rows: "))

for i in range(n):
    for j in range(i-1):
        print(i+1,end=" ")
    print()


#decreasing pattern
n=int(input("enter rows"))
for i in range(n,0,-1):
    for space in range(n-i):
        print(" ",end=" ")

    for j in range(i):
        print("* ",end=" ")
    print()


#reverse a string
a=input()
rev=""
for i in a:
    rev=i+rev
print(rev)

#reverse number
n=int(input())
for i in range(n,0,-1):
    print(i)

#palindrome
str1=input("enter string")
rev=""
for i in str1:
    rev=i+rev

if (str1==rev):
    print("palindrome")
else:
    print("not palindrome")


#largest number
n=[23,76,97,56,46,89]
large=n[0]
for i in n:
    if i>large:
        large=i
        
print(large)


#second largest
arr = [10, 45, 356, 45768, 23,543,6543]

largest = float('-inf')
second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
print("Second Largest:", largest)

def add(a):
n=int(input())
if n==2:
    Return True
for i in range(1,n+1):
    if n%i==0:
        Return False
return True
a=4
print(add(a))
    
