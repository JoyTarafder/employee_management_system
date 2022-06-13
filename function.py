
# def add_two_value(first, second):
#     return first + second

# num1 = int(input("N1 = "))
# num2 = int(input("N2 = "))

# sum = add_two_value(num1, num2)

# print("Add Two Value : ", sum)

def namefac(fastName,  lastName , middleName = ''):
    if middleName:
        fullName = f"{fastName} {middleName} {lastName}"
    else:
        fullName = f"{fastName} {lastName}"
    return fullName.title()

Name = namefac('Joy', 'Tarafder')
print(Name)
Name = namefac()
print(Name)