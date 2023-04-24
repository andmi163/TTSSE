# Input parameters
a = 15
b = 2

# Addition 
def add_nums(num1, num2):
    total = num1 + num2
    print(num1,"+",num2,"=",total)

add_nums(a,b)

# Subtraction
def sub_nums(num1,num2):
    if num1 > num2:
        total = num1 - num2
        print(num1,"-",num2,"=",total)
    else:
        total = num2 - num1
        print(num2,"-",num1,"=",total) 

sub_nums(a,b)

# Multiplication
def mult_nums(num1,num2):
        total = num1 * num2
        print(num1,"*",num2,"=",total)
