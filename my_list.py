employee_1 = 10
employee_2 = 20
employee_3 = 30
employee_4 = 40
employee_5 = 50
employee_6 = 60
employee_7 = 70

#print out the value of the employees

employees =[10, 20, 15, 30, 40, 50, 60, 70]
print(employees)

#Remove the last value
employees = ['10','20','15','30','40','50','60','70']
employees.remove('70')

print(employees)

#arrange in assending order
employees = ['10','20','15','30','40','50','60','70']
sorted_employees = sorted(employees)  # Sorted in ascending order
print("Sorted in ascending order:", sorted_employees)

#find and print the index of the value 30 in my_list.
employees = ['10', '20', '15', '30', '40', '50', '60', '70']
value_to_find = '30'  # Corrected to a string
index = employees.index(value_to_find)
print(f"The value {value_to_find} is found at index {index}")

