
str = "Hello World"

print("String is %d bytes long" % len(str))

print(str.upper())

print("The index of the o is %d" % str.upper().index("O"))

print("There are %d letter L's in '%s'" % (str.upper().count("L"), str))

#slice the string
print(str[3])
print(str[1:6])
print(str[1:len(str)])

name = "Robert Robedillo"
mylist = name.split(" ")
print(mylist)
print("My First Name is: %s and my Last Name is: %s" %(mylist[0],mylist[1]))
