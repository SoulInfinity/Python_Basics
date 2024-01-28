# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number"))
    assert num%2 == 0
    '''if num<1:
        raise Exception("No negetive number")'''
except:
    print("must be even and non negetive")

else:
    reciprocal = 1/num
    print(reciprocal)
finally:
    print("program executed successfully")

