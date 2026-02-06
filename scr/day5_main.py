def greed():
    print("Hi,I Am Syed Ameer Hamza Hussaini")
    
greed()


def welcome():
    print("Welcome to day 5 of our internship")

welcome()




def add(a,b):
    print(3+5)
result=add(3,5)
print(result)

def sub(a,b):
    print("c",(10-5))

    


X=10
def show_variable():
    X=20
    print(X)
    
show_variable()
print(X)
    


import math
import random
print(math.sqrt(10))
print(random.randint(5, 10))
    

import utils_day5


print(utils_day5.add(3, 4))
print(utils_day5.sub(3,4))
print(utils_day5.multiplication(100, 1.325))


#task1
def calc_rectangle(length, width):
    area = length*width
    perimeter = 2 * (length+width)
    return area, perimeter

length=int(input("Enter Length:"))
width=int(input("Enter width:"))
area, perimeter=calc_rectangle(length, width)
print(f"Area: {area}, perimeter: {perimeter}")

#Another Way(you can take float instead of int "let's take and try")
def calc_rectangle(length, width):
    area = length*width
    perimeter = 2 * (length+width)
    return area, perimeter

length=float(input("Enter Length:"))
width=float(input("Enter width:"))
area, perimeter=calc_rectangle(length, width)
print(f"Area: {area}, perimeter: {perimeter}")



#task2
import math_operations

print(math_operations.power(2, 10))
print(math_operations.average([10,20,30,40]))



