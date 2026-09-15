#q2
marks = 20

if marks >=90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >=50:
    grade = "Pass"
else: grade = "Fail"

print(f"Marks: {marks} Grade: {grade}")

#3
#Multiplication of 3 table using for loop
word = int(input("enter a number"))
for x in range(1,13):
    print(f" 3x{x} = {3*x*word}")

#q5 
numbers = [88, 72, 95, 72, 61, 88, 83, 95,50]

# Remove duplicates
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

# Find total, highest and lowest
total = 0
highest = unique[0]
lowest = unique[0]
passing = 0

for number in unique:
    total += number

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number
    if number >= 60:
        passing +=1
    

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
print(f"number of students passing{passing}")



#q8

python_students = {"Aman", "Rahul", "Sara", "Priya"}
both = {"Aman", "Priya", "Arjun"}
sql_students = {"Rahul", "Priya", "Arjun", "Neha"}
print(f"python students{python_students}")
print(f"student doing both {both}")
print(f"sql students {sql_students}")


student = {
    "name": "jassim",
    "age": 16,
    "course": "python,statistics and sql"   
}
print(student)
print(student["name"])

subjects = ["python marks", "statistics marks", "sql marks"]
marks_maths = [88, 98, 45, 87]

for name, score in zip(subjects, marks_maths):
    grade = "A" if score >=90 else "B" if score >=50 else "fail"
    print(f"{name} {score} Grade: {grade}")





    
