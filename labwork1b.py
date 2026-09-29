students=[]
courses=[]
marks={}
student_mark_management= {"students":students,"courses":courses,"marks":marks}

def numberofstudent():
    return int(input("Enter the number of students:"))
n=numberofstudent()

def student_info():
    for i in range(n):
        id= int(input("Enter id:"))
        name= input("Enter your name:")
        Dob=  input("Enter your Dob:").split()
        students.append([id,name,Dob])
student_info()

def courses_info():
    courses_count=int(input("Enter number of course:"))
    for i in range (courses_count):
        course_id= int(input("Enter your course's id:"))
        course_name= input("Enter your course's name:")
        courses.append([course_id,course_name])
courses_info()

def mark_info():
    for c_id, c_name in courses:
        marks[c_id] = {}
        print(f"Course {c_name}:")
        for s_id, s_name, s_dob in students:
            marks[c_id][s_id] = float(input(f"Enter mark of student {s_name}:"))
mark_info()

for c_id, c_name in courses:
    print(f"Course {c_name}:")
    for s_id, s_name, s_dob in students:
        print(f"- Student {s_name}, ID {s_id}, DOB {s_dob}")
        print(f"  {marks[c_id][s_id]}")