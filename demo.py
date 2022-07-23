f = open('demo.txt', 'a')
a = input("Name : ")
p = input("Pass : ")
x = a + " " + p + "\n"
f.write(x)
# f.write('Demo')
# print(f.read())


f.close()