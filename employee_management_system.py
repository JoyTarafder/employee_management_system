employee_list = []


def print_employee_list():
    if employee_list == []:
        print("This employee list is empty")
    else:
        print("Employee List:")
        print("-------------")
        print("ID      Name            Salary")
        for i in range(0, len(employee_list)):
            print("{0:6}  {1:12}  {2:7}".format(employee_list[i][0], employee_list[i][1], employee_list[i][2]))


def insert_employee():
    # Ask for employee detail
    print("****** Enter new employee details ******")
    employee_ID = input("Insert the ID of the new employee: ")

    found = False
    for i in employee_list:
        # Cheak same ID
        if i[0] == employee_ID:
            print("\nThis ID already exists.\nPlease enter new ID.")
            found = True

    if found == False:
        # Adding new employee
        employee_name = (input("Insert the name of the new employee: ")).title()
        employee_salary = float(input("Insert the salary of the new employee: "))
        New_employee = [employee_ID, employee_name, employee_salary]
        employee_list.append(New_employee)


def delete_employee():
    # delete employee
    found = False
    id = input("Enter Employee ID : ")
    for i in employee_list:
        if i[0] == id:
            employee_list.remove(i)
            print("Remove the employee successful.")
            found = True
    if found == False:
        print("This id has not been found")


def print_highest_paid_employee_name():
    if employee_list == []:
        print("This employee list is empty")
    else:
        employee_salary_list = []
        for i in range(0, len(employee_list)):
            employee_salary_list.append(employee_list[i][2])

        employee_high_salary = max(employee_salary_list)

        for j in range(0, len(employee_list)):
            if employee_list[j][2] == employee_high_salary:
                print("Highest paid employee name : ", employee_list[j][1])

print(" \n****** Employee Management System for IUB - Log in ******")
print("------------------------------------------------------------")
userName = input("Enter Your Username : ")
password = input("Enter Your Password : ")

if userName == "JoyT" and password == "joytarafder":
    option = 0
    while option != 5:  # Exit loop when the value is 5
        print(" ****** Employee Management System for IUB ******")
        print("---------------------------------------------------")
        print("1 -> Insert employee")
        print("2 -> Delete employee")
        print("3 -> Print all employee")
        print("4 -> Print the name of the highest paid employee")
        print("5 -> Exit")
        option = int(input("Select an option (1/2/3/4/5): "))
        print("\n")  # For new line

        # Check chosen option and call the appropriate function
        if option == 1:
            # Call the insert_employee() function
            insert_employee()
            print("\n")  # For new line
        elif option == 2:
            # Call the delete_employee() function
            delete_employee()
            print("\n")  # For new line
        elif option == 3:
            # Call the print_employee_list() function
            print_employee_list()
            print("\n")  # For new line
        elif option == 4:
            # Call the print_highest_paid_employee_name() function
            print_highest_paid_employee_name()
            print("\n")  # For new line
        elif option == 5:
            # Exit
            print("\n")  # For new line
        else:  # Wrong Input (option < 0  and option > 5)
            print("Wrong Input\nTry again")
            print("\n")  # For new line
else:
    print("\nInvalid User ID")