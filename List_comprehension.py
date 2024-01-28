h = []
for i in "human":
    h.append(i)
print(h)
#Method 2
h = [i for i in "human"]
print(h)
# method 3
list = [x for x in range(20) if x%2 == 0]
print(list)
#using nested if
list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(list)
# using else statement
num = ["even" if i % 2 == 0 else "Odd" for i in range(10)]
print(num)