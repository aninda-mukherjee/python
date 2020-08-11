
emp_file = open("employees.txt", "r")
print(emp_file.readable())
print(emp_file.read())
print(emp_file.readline())
print(emp_file.readlines())
print(emp_file.readlines()[1])

for employee in emp_file.readlines():
    print(employee)
emp_file.close()