'''list1=[]
even_list=[]
odd_list=[]
size=int(input("entre years no"))
for i in range(size):
    ele=int(input("enter year"))
    list1.append(ele)
    if ele%4==0 and ele%400==0 and ele%100==0:
       even_list.append(ele)
    else:
       odd_list.append(ele)
print("original list",list1)
print("even number list",even_list)
print("odd number list",odd_list)'''




'''graph = { '5':['3','7'], '3':['2','4'], '7':['9'], '2':[], '4':['8'], '8':[] }
visited = set()
def dfs(visited, graph, node):
   if node not in visited:
      print(node)
      visited.add(node)
      for neighbour in graph[node]:
         dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '5')'''






# Programm No.5
'''import numpy as np
import random
from time import sleep
def create_board():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    if selection:  
        current_loc = random.choice(selection)
        board[current_loc] = player
    return board

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                break
        if win:
            return True
    return False

def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True
    win = True
    for x in range(len(board)):
        if board[x, len(board) - 1 - x] != player:
            win = False
            break
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            break
    if np.all(board != 0) and winner == 0:
        winner = -1  # Tie
    return winner

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move(s):")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
print("Winner is:", play_game())'''









'''
# programm no.6
import copy
from heapq import heappush, heappop

# Puzzle dimensions (3x3)
n = 3

# Directions for movement (up, left, down, right)
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

# Priority Queue for A* search
class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap

# Node class for the state of the puzzle
class node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    # Comparison operator for priority queue
    def __lt__(self, nxt):
        return self.cost < nxt.cost

# Function to calculate the cost (misplaced tiles)
def calculateCost(mat, final):
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and mat[i][j] != final[i][j]:
                count += 1
    return count

# Generate a new node by moving the empty tile
def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
    new_mat = copy.deepcopy(mat)

    # Swap tiles
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Calculate cost and create a new node
    cost = calculateCost(new_mat, final)
    return node(parent, new_mat, new_empty_tile_pos, cost + level, level)

# Check if a position is within bounds
def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

# Print the matrix
def printMatrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))
    print()

# Print the path from the root to the solution
def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)

# Solve the puzzle using the A* algorithm
def solve(initial, empty_tile_pos, final):
    pq = priorityQueue()

    # Create the root node
    cost = calculateCost(initial, final)
    root = node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)

    while not pq.empty():
        # Get the node with the lowest cost
        minimum = pq.pop()
        # If he goal state is reached, print the solution
        if minimum.cost - minimum.level == 0:
            printPath(minimum)
            return
        # Explore all possible moves
        for i in range(4):
            new_tile_pos = [
                minimum.empty_tile_pos[0] + row[i],
                minimum.empty_tile_pos[1] + col[i],
            ]
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                # Create a child node and push it into the queue
                child = newNode(
                    minimum.mat,
                    minimum.empty_tile_pos,
                    new_tile_pos,
                    minimum.level + 1,
                    minimum,
                    final,
                )
                pq.push(child)
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_pos = [1, 2]
solve(initial, empty_tile_pos, final)







table = int(input("Enter a Number : "))
i=1
while i<=10:
    print(table,"X",i,":",table*i)
    i += 1



table = int(input("Enter a Number : "))
for i in range(1,21):
    print(table * i)'''



'''string=["Ironman","Thor","CapAmerica","Hulk","Docter Doom"]
i=0
while i < len(string):
    print(string[i])
    i += 1'''



'''string=["Ironman","Thor","CapAmerica","Hulk","Docter Doom"]
for i in string:
    print(i)'''



'''n=[1,4,9,16,25,36,49,64,81,100]
for i in n:
    print(i)'''


'''n=[1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(n):
    print(n[i])
    i += 1


nums=[1,4,9,16,25,36,49,64,81,100]
target = 49
i=0
while i<len(nums):
    if(nums[i] == target):
        print(nums[i],"found at Index No. : ",i)
    i += 1




nums=[1,4,9,16,25,36,49,64,81,100]
target = 49
index = 0
for i in nums:
    if(i == target):
        print(i,"found at Index No. : ",index)
    index += 1





def BinarySearch(nums, target):
    s=0
    e=len(nums)-1
    while s <= e:
        mid=s+(e-s)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return -1

nums = [2,5,6,7,8]
target = 7
print(BinarySearch(nums, target))






n=int(input("Enter a number : "))
sum=0
for i in range(1, n+1):
    sum += i
print("sum of all numbers : ",sum)






n=int(input("Enter a number : "))
sum=0
i=0
while i<=n:
    sum += i
    i += 1
print("sum of all numbers : ",sum)



def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
n=5
print(fact(n))



n=5
fact=1
for i in range(1, n+1):
    fact *= i
print(fact)



def calSum(a,b):
    return a+b
print(calSum(2,5))



def length(s):
    return s
s=["Delhi","Mumbai","Noida","Gurugram"]
print(length(len(s)))



def length(s):
    for i in s:
        print(i, end =" ")
s=["Delhi","Mumbai","Noida","Gurugram"]
length(s)



def length(s):
    for i in s:
        print(i)
s=["Delhi","Mumbai","Noida","Gurugram"]
length(s)



def length(s):
    for i in s:
        return s
s=["Delhi","Mumbai","Noida","Gurugram"]
print(length(s))


def DollarToIndian(n, dollar):
    rupees = n * dollar
    return rupees

n=int(input("Enter No. of dollar : "))
dollar=86.67
print(DollarToIndian(n,dollar))



def EvenOdd(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
n=int(input("Enter a numbe : "))
EvenOdd(n)




a=[2,9,6,10,8,11,15]
INT_MIN=-2**31
largest = INT_MIN
s_largest = INT_MIN
for i in a:
    if i > largest:
        s_largest = largest
        largest = i
    elif i > s_largest and i < largest:
        s_largest = i

print("Second largest element is :",s_largest)





def fib(n):
    a = 0
    b = 1
    for i in range (1, n+1):
        c = b
        b = a+b
        a = c
    return b
n = int(input("Enter A No. which you that he is fibonacci or not : "))
print(fib(n))'''



# def show(n):
#     if(n == 0):
#         return
#     return(n-1)
# print(show(5))




# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n
# print(sum(5))




# def List(a, idx):
#     if(idx == len(a)):
#         return
#     print(a[idx])
#     return List(a, idx + 1)
# a = ["Tasleem", "Ankit", "Vaibhav", "Sujal"]
# idx = 0
# List(a, idx)





# list = [1,2,3,4]
# list.append(5)
# list[4]=6
# print(list) 


# list = ['a','c','b','g','f']
# list.sort()
# print(list)


# list = ['a','c','b','g','f']
# list.sort(reverse = True)
# print(list)


# list = ['a','c','b','g','f']
# list.reverse()
# print(list)


# list = ['a','c','b','g','f']
# list.insert(1, 'b')
# print(list)



# list = ['a','c','b','g','f']
# list.remove('a')
# print(list)


# list = ['a','c','b','g','f']
# list.pop(1)
# print(list)




# tup = (1,2,3,4,5,6,7,8)
# print(tup)



# movies = []
# n=int(input("Enter Movies No. : "))
# for i in range(n):
#     n1=input(f"Enter Movies name {i+1}: ");
#     movies.append(n1)
# print(movies)

 


# s = "racecar"
# st = 0
# e = len(s)-1
# is_palindrome = True
# while st <= e:
#     if s[st] != s[e]:
#         is_palindrome = False
#         break
#     st += 1
#     e -= 1
# if is_palindrome:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")


# s="racecar"
# t=s[::-1]
# if s == t:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")



# l=[1,2,3]
# s=l.copy()
# l.reverse()
# if l == s:
#     print("Palindromic list")
# else:
#     print("not a palindromic list")



# n=12321
# t=n[::-1]
# if n == t:
#     print("String is a palindrome")
# else:  
#     print("String is not a palindrome")




# student = {
#     "Name" : "Tasleem Shah",
#     "Subject" : {
#         "Math" : 95,
#         "Eng" : 96,
#         "Science" : 98
#     },
#     "Age" : 27,
#     "color":"White"
# }
# print(student)



# student = {
#     "Name" : "Tasleem Shah",
#     "Subject" : {
#         "Math" : 95,
#         "Eng" : 96,
#         "Science" : 98
#     },
#     "Age" : 27,
#     "color":"White"
# }
# print(student.keys())
# print(student.values())


# student = {
#     "Name" : "Tasleem Shah",
#     "Subject" : {
#         "Math" : 95,
#         "Eng" : 96,
#         "Science" : 98
#     },
#     "Age" : 27,
#     "color":"White"
# }
# print(student.items())



# student = {
#     "Name" : "Tasleem Shah",
#     "Subject" : {
#         "Math" : 95,
#         "Eng" : 96,
#         "Science" : 98
#     },
#     "Age" : 27,
#     "color":"White"
# }
# print(student["Name"])
# print(student.get("Name"))



# student = {
#     "Name" : "Tasleem Shah",
#     "Subject" : {
#         "Math" : 95,
#         "Eng" : 96,
#         "Science" : 98
#     },
#     "Age" : 27,
#     "color":"White"
# }
# student.update({"City" : "Kanpur"})
# print(student)




# Set in pyhton
# nums={1,2,3,4,5,6,6,"Hello","Hello"}
# print(nums)



# s=set()
# s.add(1)
# s.add(3)
# s.add(8)
# print(s)
# s.remove(1)
# print(s)


# collection = {"Hello","coding","python","C++","Php"}
# print(collection.pop())



# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print("intersection of two set : ",set1.intersection(set2))



# subject= {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(subject))


# subject = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(subject))


# subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# subject_count = {}
# for sub in subjects:
#     if sub in subject_count:
#         subject_count[sub] += 1
#     else:
#         subject_count[sub] = 1

# print(len(subject_count))
# print(subject_count)



# marks={}
# x=int(input("Enter Physics Marks : "))
# marks.update({"Physics" : x})
# x=int(input("Enter Chemistry Marks : "))
# marks.update({"chemistry" : x})
# x=int(input("Enter Mathematics Marks : "))
# marks.update({"Mathematics" : x})
# print(marks) 




# f = open("data.txt","r")
# data = f.read()
# print(data)
# f.close()


# f = open("data.txt","w")
# f.write("Hey currently i am working in Accenture as a software Engineer")
# f.close()


# f = open("data.txt","a")
# f.write("\n But i want to change my domain into data scientist")
# f.close()


# with open("data.txt","r") as f:
#     data = f.read()
#     print(data)


# import os
# os.remove("data.txt")


# with open("sample.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I\O\n")
#     f.write("using Java.\nI like programming in Java.")



# with open("sample.txt","r") as f:
#     data = f.read()
# new_data=data.replace("Java","Python")
# print(new_data)

# with open("sample.txt","w") as f:
#     f.write(new_data)




# word = "learning"
# with open("sample.txt","r") as f:
#     data = f.read()
#     #if(word in data) isko aise bhi likh sakte hain
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("Not found")





# def check_for_line():
#     word = "programming"
#     data = True
#     line_no = 1
#     with open("sample.txt","r") as f:
#         while data:
#             data=f.readline()
#             #is line ko aise bhi likh sakte hain
#             #if(word.find(data) != -1):
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()



# class student:
#     name="Tasleem Shah"
# s=student()
# print(s.name)


# class Car:
#     color = "Blue"
#     brand = "mercedes"
# s=Car()
# print(s.color)
# print(s.brand)



# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
# s=Student("Tasleem Shah")
# print(s.name)
# s1=Student("Vaibhav")
# print(s1.name)




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks=marks
# s=Student("Tasleem Shah",97)
# print(s.name, s.marks)
# s1=Student("Vaibhav",99)
# print(s1.name, s1.marks)



# class Student:
#     college_name="Apna College"
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("welcome student",self.name)
#     def get_marks(self):
#         return self.marks
# s=Student("Tasleem",98)
# s.welcome()
# print(s.get_marks())



# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def Average(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print(self.name,": your average is :",sum/3)
# s=Student("Tasleem",[96,90,80])
# s.Average()



# class Student:
#     @staticmethod
#     def Hello():
#         print("Hello")
# s=Student()
# s.Hello()



# #Abstraction
# #code ke andar jab unnecessary implementation detail ko hide kar lo aur jaruri chize dikhao
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clt=False
#     def start(self):
#         self.clt=True
#         self.acc=True
#         print("car started...")
# car1=Car()
# car1.start()



# class Account:
#     def __init__(self, balance, account_no):
#         self.balance=balance
#         self.account_no=account_no

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("total balance =",self.get_balance())
    
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("total balance =",self.get_balance())
    
#     def get_balance(self):
#         return self.balance
    
# A=Account(1000, 602802010002633)
# print("Primary Balance is :",A.balance, "And my Account No. :", A.account_no)
# A.debit(200)
# A.credit(500)



