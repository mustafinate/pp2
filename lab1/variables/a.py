#ex1
carname = "Volvo"
print(carname)

#output Volvo

#ex2
x = 50
print(x)

#output 50

#ex3
x = 5
y = 10
print(x+y)

#output 15

#ex4
x = 5
y = 10
z = x+y
print(z)

#output 15

#ex5
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

#output Orange Banana Cherry

#ex6
x = y = z = "Orange"
print(x)
print(y)
print(z)

#output 
# Orange
# Orange
# Orange

#ex7
def myfunc():
  global x
  x = "fantastic"

myfunc()

print(x)

#output fantastic