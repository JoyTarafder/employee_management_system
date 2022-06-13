
# def greet_user(username):
#     print(f"Hello {username.title()}!")

# greet_user("joy tarafder")

# greet_user ("Fahim Fysal")
# name = input("Enter Your Name : ")
# print(name)
letter = '''Dear, |<NAME>|!
Congraulations! You are selected.

Best regrad
Date : |<DATE>|'''
name = input("Enter name : ")
date = input("Enter date : ")

letter = letter.replace("|<NAME>|", name)
letter = letter.replace("|<DATE>|", date)

print(letter)