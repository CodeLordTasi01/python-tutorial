''''a=[5,5,6,7,7,7]
b=set(a)
def test(lst):
    if lst in b:
        return 1
    else:
        return 0
for i in filter(test, a):
    print(i,end="")



import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70 
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(150)


from array import array
from bisect import bisect_right
t = int(input())
for _ in range(t):
    n = int(input())
    arr = array('I', [int(i) for i in input().split()])
    sarr = array('I', [arr[0]])
    result = 0
    for i in range(1, n):
        e = arr[i]
        j = bisect_right(sarr, e)       
        sarr.insert(j, e)
        result += i - j
    print(result)


A=[5,7,11,6,2,1,18,50]
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if A[i]>=A[j]:
           k=A[i]
           A[i]=A[j]
           A[j]=k
print("after sort",A)


#sum of array digit is 6
def findchange(arr, s, i):
    if(i==len(arr) and s==0):
        return 1
    if(i==len(arr) and s>0):
        return 0
    if(arr[i]>s):
        return findchange(arr, s, i+1)
    else:
        return findchange(arr, s-arr[i], i+1)+findchange(arr, s, i+1)
if __name__ == "__main__":
    arr=[4,1,3,2]
    s=6
    count=findchange(arr,s,0)
    print(count)



n=int(input())
if n%3==0 or n%5==0 or n%7==0:
    print("not power")
else:
    print("power")



n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print("*")
        j=j+1
    print('\n')
    i=i+1



int n=int(input())
int i=1
while(i<=n):
    int j=1
    while(j<=n):
        char ch='A'+j-1
        print(ch)
        j=j+1
    break;
    i=i+1



from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Lion(Animal):
    def sound(self):
        return "roar"
class Tiger(Animal):
    def sound(self):
        return "growl"
l=Lion()
print("Lion Sound:",l.sound())
t=Tiger()
print("Tiger Sound:",t.sound())


nums=[3,2,1,5,6,4]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>=nums[j]:
            k=nums[i]
            nums[i]=nums[j]
            nums[j]=k
print(k-2)




n=int(input())
a={}
for i in range(0, n+1):
    if(i%2 !=0):
        if n[i] in a:
            print(i)


s="tasleem is bad"
print(s[::-1])



n=int(input())
s=0
for i in str(n):
    while(str(len(i))!=1):
        s +=int(i)
print(s)


num = 12345
sum1 = 0
while num!=0:
	digit = (num%10)
	sum1 = sum1+digit
	num = num//10
	if sum1/10!=0:
	    num=sum1
	    sum1=0
print(sum1)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())  
stack.pop()
print(stack.peek())




n=[1,9,6,3]
d=0
e=0
for i in n:
    while i!=0:
        d=d+i%10
        i=i//10
for z in n:
    e=e+z
print(abs(e-d))





n=[100,4,200,1,2,3]
a=len(n)
res=0
d={}
for i in n:
    d[i]=1
for x in n:
    if(x-1 not in d):
        c=1
        i=1
        while(x+i not in d):
            c+=1
            i+=1
        res=max(res,c)
print(res)
        


class Solution(object):
    def longestConsecutive(self, A):
       
        n=len(A)
        res=0
        d={}
        for i in A:
            d[i]=1
        for x in A:
            if(x-1 not in d):
                c=1
                i=1
                while(x+i in d):
                    c+=1
                    i+=1
                res=max(res,c)
        return res



l=[1,2,5,4,5,2,2]
for i in range(0,len(l)):
    if l[i]==2 and l[i+1]==2:
        print(True)
print(False)




class A:
    def add(self,x,y):
        return x+y
class B(A):
    def add(self,x,y,z):
        self.z=z
        return x+y+z
obj=B()
print(obj.add(7,8,10))



class child:
    a=9   # static
    def add(self,x,y):
        self.z=5   # instance variable
        h=6   # h,x,y are local variable
        return x+y+self.z

objchild=child()   # objchild reference variable
print(objchild.add(4,5))
print(objchild.z)    # accessing of instance variable
print(child.a)    # accessing of static variable





def Display(name,*city):
    print(name)
    print(city)
Display("Ayush","Kanpur","Lucknow","delhi")




a={1,'S',7.8}
b=set([1,'B',6.9,])
b.add("TASLEEM")
c=frozenset(b)
print(a)
print(b)
print(c)





import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert_at_begin():
    global head
    item = int(input("Enter the item for insert: "))
    ptr = Node(item)
    if ptr is None:
        print("overflow")
    else:
        ptr.next = head
        head = ptr

def display():
    global head
    ptr = head
    while ptr is not None:
        print(f"{ptr.data}->", end="")
        ptr = ptr.next
    print("NULL")

def delete_at_begin():
    global head
    ptr = head
    head = ptr.next
    del ptr

def main():
    global head
    while True:
        print("1.Insert at begin\n2.Display\n3.Delete at begin\n4.Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert_at_begin()
        elif choice == 2:
            display()
        elif choice == 3:
            delete_at_begin()
        elif choice == 4:
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



class Student:
    def __init__(self,name,roll_no,clg):
        self.name=name
        self.roll_no=roll_no
        self.clg=clg
    def print_Detail(self):
        print("name = ",self.name)
        print("Roll No. = ",self.roll_no)
        print("college = ",self.clg)
obj1=Student("raj",123,"psit")
obj1.print_Detail()
'''


'''
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        n=len(nums)
        rem=sum(nums)%p
        if(rem==0):
            return 0
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]
        for i in range(n):
            nums[i]=nums[i]%p
        res=9999999
        d={0:-1}
        for i in range(n):
            if((nums[i]-rem)<0):
                if(nums[i]-rem+p in d):
                    res=min(res,i-d[nums[i]-rem+p])
            else:
                if(nums[i]-rem in d):
                    res = min(res,i-d[nums[i]-rem])
            d[nums[i]]=i
        if(res==n):
            return -1
        else:
            return res





def fun(A,P):
    rem=sum(A)%p
    n=len(A)
    for i in range(1,n):
        A[i]=A[i]+A[i-1]
    for i in range(n):
        A[i]=A[i]%p
    res=10**6

d={0:-1}
for i in range(n):
    if((A[i]-rem)<0):
        if(A[i]-rem+p in d):
            res=min(res, i-d[A[i]-rem+p])
    else:
        if(A[i]-rem in d):
            rem=min(res, i-d[A[i]-rem])
    d[A[i]]=i
print(res)
'''


'''s="My college name is PSIT"
print(s[::-1])'''



s = "My college name is PSIT"
r =' '.join(s.split()[::-1])
print(r)









      
        





















        

       
    
