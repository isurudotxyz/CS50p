#  getting   input from  a file and manipulating the datas
# with open("students.csv") as file:
#     for line in file:
#         # separating each line content by the , and assign it a row variable
#         name, house = line.rstrip().split(",")
#         # ]
#         print(f"{name} is in {house}")
import csv

students = []

with open("students.csv") as file:
    # using csv library
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"home":row["home"]})
    
    # ----------------------   vanilla python
    # for line in file:
    #     name, home = line.rstrip().split(",")
    #     # students.append(f"{name} is in {house}"
    #     student = {"name":name,"home":home}
    #     students.append(student)
# for student in sorted(students):
# print(student)


# sort by key 

def get_name(student):
    return student["name"]
def get_house(student):
    return student["house"]


#  u can apply a function as a key parameter
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name'] is from {student['home']}}")