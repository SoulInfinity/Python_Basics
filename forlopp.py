myset = {'hello','hi','how','mine'}
print(myset)
for i in myset:
    print(i)
# for--> is a keyword
# i-->a variable(to access each element)
#in-->keyword-- It is a Membership operator
#mystate--> is a sequence(may be set,string,list or tuple)
for i in myset:
    print(i,end="")
for state in myset:
    print(i,end=" ")
for i in [2,4,6,10]:
    print(i, end="^")
    if i == 10:
        end = " "
#range() -- is a method which generates series form start to end of given values
#WAP to print your name 10 times using for and range methods
for i in range(0,11):
    print("Ashutosh")
for i in range(10):
    print("Ashutosh",end = " ")
print("hello world")
for i in range(5,55,5):
    print(i,end=' ')
num = int(input("Enter the number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
d1 = {1:10,2:30,4:80,80:12}
print(type(d1))
print(d1.values)
print(d1.keys())
print(d1.values())
d2 = {1:"one",2:"two",3:"three"}
print(d2)
d3 = {"O":"Odisha","AP":"Andhra Pradesh","UP":"Uttar Pradesh"}
d4 = {"One": 1,"two":2,"three":3}
print(d4)
d5 = {"colors":["blue","green"],"House":"2bh"}
print(d5.keys())