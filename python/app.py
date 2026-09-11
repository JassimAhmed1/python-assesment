# print program
"""
print("hello world")
print('hello world')

print("'this is a class of multiple student's where they are joining")
"""
#name = "john" #str
#phone = 1234567890 #int
#print("name:",name)
#print("phone:",phone)
#print(name + str(phone)) #type casting

f = 9.45 #float variable
i = 7890 #integer variable
b = True #boolean variable
c = "This is a string variable" #string variable

#practice question 

#Name = "Jassim"
#Phone = "89989898"
#num1 = int(input("enter first number"))
#num2 = int(input("enter second number"))
#print(num1+num2)
#print("my name is ",Name,"my phone number is ",Phone)


#practice x=10 and y=20 swap their values without a third variable
#correct answer
x = 10
y = 20
x,y = y,x

#roughwork
#word = print(y-x) #y
#print(word)

#cloud = print(x+x)#x
#print(cloud)

#name = input("what is your name?")
#number = input("what is your phone number?")
#college = input("name of your college?")
#print(name,number,college)

#age = int(input("what is your age"))
#year = 2026 - age
#print("you were born in the year of",year)

"""
fruits = ["apple", "banana", "orange", "pear", "kiwi"]
fruits.append("blueberry") #append adds value at the last of the list
print(fruits)


fruits.insert(2,"mango") #inserting
print(fruits)


#change the values
p = [11,2,3,4,5] #chnage index 3 value to 40
p[1] = 20
p[3] = 40
p[4] = 50
print(p)

#extend
p.extend([6,7,8,9,10,]) #extending values to the list
print(p)

#remove
g = [11,12,13,14,15,]
g.remove(13)
print(g)

#pop
g.pop(1) #removing the index value number
print(g)

#delete
del g[2]
print(g)

#clear
g.clear()
print(g)

#List length
lst = [1,32,73,74,65,99]
print(len(lst))
"""

# 1practice question user asks for a  of seconds and convert it into  h m s
"""
total = int(input("enter the number of secs"))
hours = total//3600
remaining_seconds = total % 3600
minute = remaining_seconds // 60
second = remaining_seconds % 60
print(f"hours:{hours}")
print(f"minutes:{minute}")
print(f"seconds{second}")
""" 
"""
#2practice 
width = float(input("enter width:"))
height= float(input("enter height:"))

area = width*height
perimeter = width*2+height*2
print(f"area:{area}")
print(f"perimeter:{perimeter}")

#3practice
bill = float(input("enter the total bill"))
ppl =  int(input("how many people in a table that will be splitting the bill"))

share = bill//ppl
print(f"your share:{share:.2f}") 
""" 
"""
name = ["apple", "sam", "huawei", "no", "redmi", "xiomi", "oppo", "oppo","realme","oneplus","google","tesla","nissian","mercedes","thar","bmw","rolls royce","hyundai","honda","samsungS24"]
print(name[3:12]) #0:0 start:end in this e.g 3:12 is the values being printed between them
print(name[-1]) # -1 is the last value of a list
name.insert(5,"Jeepv32") #inserting a value at a given index of choice
print(name)
name [-1] = "nokia" #swapping index value in a list
print(name)

# checking element
b = ("apple","mango","pineapple","jackfruit")
print("orange" in b)

#sorting list
q = [66,98,45,20,10]
q.sort()
print(q) #asceding order

#descedingi order
q.sort(reverse=True)
print(q)

#reverse
q.reverse()
print(q)

#copying list
num = [1,2,3,4,5]
num1 = num.copy()
print(num1)

#count
e = [5,6,5,9,5,9,9]
print(e.count(9))

#finding index
print(e.index(5)) #finding the index value in a list 5 in this list is at 0 index value so the code shows the output of the index value 5 is at

# If else

marks = 20

if marks >=90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else: grade = "F"

print(f"Marks: {marks} Grade: {grade}")

# Nested if #if statement in another if statement
age = 10
has_id = True

if age >=18: #1st condition
    if has_id: #2nd condition
        print("Access Granted")
    else:
        print("ID required")
        
else:
    print("Denied Access")
"""
"""
#range printing mutiple times but with a simple function of range to print
for i in range(1,6): # i is the variable range the function (1,6) value
    print(f"Student {i}")
    
# For Loop 
scores = [88, 72, 95, 61, 83,]
for result in scores:
    print(result)
    
#While Loop
count = 1
while count <= 5:
    print(count)
    count +=1


#Multiplication of 3 table using for loop
for x in range(1,13):
    print(f" 3x{x} = {3*x}")


# print numbers from 10 using while loop
number = 10
while number >=1:
    print(number)
    number -=1
 """   
# Break and Continue 
for i in range(1,11): #printing from 1,11 range
    if i ==3: # 3 gets skipped
        continue # in continue 3 is skipped, it contiunues upto 11(not inclusive here in this code bc of index)
    #if there was break on line no 219 then the values only go upto 1 to 3 "break" it doesnt continue and skip the given number line218
    print(i)
#

#assignment
"""
menu = ["sandwich:£5", "pizza:£6", "burger:£7","orange:£2","sprite:£3"]
print(menu)
sandwich1 = 5
pizza1 = 6
burger1 = 7
orange1 = 2
sprite1 = 3
sandwich = int(input("enter the number of sandwich"))
pizza = int(input("enter the number of pizza"))
burger = int(input("enter the number of burger"))
orange = int(input("enter the number of orange"))
sprite = int(input("enter the number of sprite"))

total = sandwich*sandwich1+pizza*pizza1+burger*burger1+orange*orange1+sprite*sprite1
gst = 0.18
bill = total*gst
print(f"here is the bill including gst:  £{total-bill}")
"""
#assignment 2
"""
ticket = ["silver:$10", "gold$20", "platinum$30"]
print(ticket)
silver1 = 10
gold1 = 20
platinum1 = 30

silver = int(input("enter the number of silver tickets")) 
gold = int(input("enter the number of gold tickets "))
platinum = int(input("enter the number platinum tickets"))

total = silver*silver1+gold*gold1+platinum*platinum1
gst = 0.12
bill = total*gst
print(f"here is the bill including gst ${total-bill}")
"""
#Section B Coding Fundamentals
"""
#number 6 number pattern
print("*")
print("**")
print("***")
print("****")
print("*****")

#Qs.7 even and odd counter
lst = []
print("enter 10 numbers")
for i in range(10):
    ask = int(input(f"Enter your number {i+1}: ") )
    lst.append(ask) 
print(lst)
 
    
#Qs.8 student mark display
"""
"""
marks = [90, 85, 75, 67, 56, 45, 43, 40]
highest_mark = print(f" this is the highest mark {marks[0]} ")
lowest_mark = print(f"this is the lowest mark {marks[7]}")
average_mark = marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5]+marks[6]+marks[7]
avrge_mark = average_mark//7
print(f"This is the average mark{avrge_mark}")

#Qs.9 multiplication table
num = int(input("enter a number"))
for x in range(1,11):
    print(f" {num}x{x} = {num*x}")
"""
"""

#Section C Mini Building projects



#taking a single value and storing in a list
mylst = []

uservalue = int(input("enter a number"))

mylst.append(uservalue)
print(mylst)

#Store Multiple Values Using a Loop
"""
"""
my_liststudent = []
mylistmark = []


#Qs.10 
for i in range(5): #loop 5x
    item = input(f"Enter enter student name {i+1}: ") # input will ask 5x +1 to say enter item 1 looping starts from 0
    my_liststudent.append(item) # my list is the list variable, item variable taking values, append adds the values at the end which these brackets starts from the beginning,[]

print(my_liststudent)

for x in range(5): #loop thrice
    mark = int(input(f"Enter enter student marks {x+1}: ")) # input will ask thrice +1 to say enter item 1 looping starts from 0
    mylistmark.append(mark) # my list is the list variable, item variable taking values, append adds the values at the end which these brackets starts from the beginning,[]

print(mylistmark)

for my_liststudent, mylistmark in zip(my_liststudent, mylistmark):
    print(f"{my_liststudent} scored {mylistmark}")
# Bonus Number Guessing Game

number = 23
print("Welcome to the number guessing game")
print("You have 5 attempts")

for o in range(5):
    guess = int(input(f"Enter guess {o+1}: "))

    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is correct!")
        break  
"""

numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print(total) #15


# Accumulator patter
scores = [88, 72, 95, 61, 83,]
total = 0
highest = 0
passing = 0

for score in scores:
    total += score
    if score > highest:
        highest = score
    if score >= 50:
        passing +=1

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average: .1f}")
print(f"Highest: {highest}")
print(f"Passing: {passing} out of {len(scores)}")

# enumerate() attaching the index values
m_students = ["aarav", "sneha", "rohan", "abhi" ]

for i, name in enumerate(m_students, start=1):
    print(f"{i} . {name}")

#zip()
names = ["Arav", "sneha", "rohan", "abhi"]
marks_maths = [88, 98, 45, 87]

for name, score in zip(names, marks_maths):
    grade = "A" if score >=90 else "B" if score >= 75 else "C"
    print(f"{name} {score} Grade: {grade}")

# Q1 - Accumaltor pattern
#Given a list of numbers, find the total average lowest and count of numbers above 50
scores = [88, 72, 95, 61, 83]  # Removed trailing comma

total = 0
lowest = scores[0]    #based on the index value
passing = 0

for score in scores:
    total += score # summing up all the numbers
    if score < lowest: # the loop to check each value from the list to check the smallest number
        lowest = score
    if score >= 50: # counting scores above 50
        passing += 1

average = total / len(scores)

print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} out of {len(scores)}")

#Q2 - Enumerator()
#Given a list of student names and marks use enumerate() to print each student's number, name, and marks

#m_students = ["aarav;50", "sneha:67", "rohan:78", "abhi:89" ]
#mark = [56, 67, 45, 89]

#for i, name in enumerate(m_students, mark):
#    print(f"{i} . {name}")

m_students = ["aarav", "sneha", "rohan", "abhi"]
mark = [56, 67, 45, 89]

# zip combines the lists, enumerate adds the counter
for i, (name, score) in enumerate(zip(m_students, mark), start=1):
    print(f"{i}. {name} - Marks: {score}")

# Q3 - zip()
#given two lists containing student name and marks, use zip() to display each student's names, marks, and grade based on their score 

    names = ["Arav", "sneha", "rohan", "abhi"]
marks_maths = [88, 98, 45, 87]

for name, score in zip(names, marks_maths):
    grade = "A" if score >=90 else "B" if score >= 75 else "C"
    print(f"{name} {score} Grade: {grade}")




# Functions
#It is a reusbale block of code
#adv - less code, predefine by user
#Functions def()
#def fuction_name():
    #function body

def greet(): #def is the keyword used to create the function / greet() is the function name
    print("Welcome to Python!")
greet() #calls the function (executes)

def greet(name):
    print("hello", name) 
greet("Afnan")

# Multiple parameters
def add(a,b):
    print(a+b)
add(10,20)

#Return Statement

def add(a,b):
    return a+b
result = add(10,20)
print(result)

#tuples used when you want to store multiple values together and you don't want those values to be changed
numbers = (10, 20, 30, 40)
print(numbers.index(30))

x = (24, 45, 56, 67, 80)
print(x.index(45,))

#Instead of:
student = ["Ayman", 18, "python"]

#dictionary when you want to store related information with labels . 
student = {
    "name": "faiz",
    "age": 18,
    "course": "python"   
}
print(student)
print(student["name"])

#set is a collection used to store unique values
numbers = {10, 20, 30, 20, 10}
print(numbers)

#List: values + duplication + index
#Tuple: values + duplicates + cannot change
#Dictionary: key +

#Q1 — List
#Given a list of numbers, remove duplicate values without using set(), then find the highest, lowest, total, average, and second-highest value.

numbers = [88, 72, 95, 72, 61, 88, 83, 95]

# Remove duplicates
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

# Find total, highest and lowest
total = 0
highest = unique[0]
lowest = unique[0]

for number in unique:
    total += number

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

# Find average
average = total / len(unique)

# Find second highest
sorted_numbers = sorted(unique)
second_highest = sorted_numbers[-2]

print(f"Unique values: {unique}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Second highest: {second_highest}")