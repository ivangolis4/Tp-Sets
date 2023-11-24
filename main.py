students = {}

def length():
    try:
        return int(input("How many students do you like to enroll:"))
    except ValueError:
        return length()




i = length()

for i in range(i):
    i = i + 1
    id = input("Enter Student number "+str(i)+": ")
    name = input("Enter first name "+str(i)+": ")
    students[id] = name


print("Student List;")
for keys, value in students.items():
    print(keys, value)


id = input("Enter Student number: ")
name = input("Enter first name: ")
students[id] = name

print("Student List;")
for keys, value in students.items():
    print(keys, value)