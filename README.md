# employee_management_system
Mr. Farid wants to build an employee management system for IUB. HELP HIM!!
This system will store employee information. First, the system will display a menu. They are:
1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

If the user selects 1, the system will take 3 inputs (ID, Name, Salary) to add a new employee.
After inserting the employee, the system will display the menu again.
If the user selects 2, the system will take 1 input (ID) to delete that employee. If the ID does not
exist, the system will print “ID not valid”. After that, the system will display the menu again.
If the user selects 3, it will print all the info (ID, name, Salary) of all existing employees. After
that, the system will display the menu again.

If the user selects 4, it will print the name of the employee who has the highest salary. After
that, the system will display the menu again.
If the user selects 5, the program will stop.

Example (Here, red color indicates user input):
1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 1

Insert the ID of the new employee: 102

Insert the name of the new employee: Sakib

Insert the salary of the new employee: 30000

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 1

Insert the ID of the new employee: 122

Insert the name of the new employee: Nafis

Insert the salary of the new employee: 50000

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 1

Insert the ID of the new employee: 450

Insert the name of the new employee: Arif

Insert the salary of the new employee: 20000

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit
 
Select an option (1/2/3/4/5): 2

Insert the ID of the employee to be deleted: 122

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 3

ID     Name   Salary

102   Sakib   30000

450   Arif    20000

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 4

Sakib

1. Insert employee
2. Delete employee
3. Print all employee
4. Print the name of the highest paid employee
5. Exit

Select an option (1/2/3/4/5): 5

(The program will stop running)

Hints:
Use dictionary to store the employees. You can use list as the value of a dictionary. Also, you
can use 2d list to do the same task.
To maintain a menu, you can use a while loop.
