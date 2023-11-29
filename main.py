import re

students = []
pattern = re.compile(r'^\d{4}-\d{4}$')
name_pattern = re.compile(r'[a-zA-Z]')

def length():
    try:
        return int(input("How many students do you like to enroll: "))
    except ValueError:
        return length()

def print_list():
    print("=====================================")
    print("Student List:")
    for student in students:
        print(student['id'], student['name'])

def update_students():
    new_id = input("Enter new Student number: ")
    if pattern.match(new_id):
        while True:
            new_name = input("Enter new first name: ")
            if name_pattern.match(new_name):
                students[2] = {'id': new_id, 'name': new_name}
                print_list()
                break
            else:
                print("Please enter a proper name.")
    else:
        print("Invalid ID format.")

isn = length()
if isn < 3:
    print("=====================================")
    print("Must have at least 3 students.")
    isn = length()
print("=====================================")

for i in range(isn):
    bl = True
    while bl:
        student_id = input("Enter Student number " + str(i + 1) + ": ")
        if pattern.match(student_id):
            while True:
                student_name = input("Enter first name " + str(i + 1) + ": ")
                if name_pattern.match(student_name):
                    students.append({'id': student_id, 'name': student_name})
                    bl = False
                    break
                else:
                    print("Invalid Name.")
        else:
            print("Invalid ID.")

print_list()
print("=====================================")
update_students()
