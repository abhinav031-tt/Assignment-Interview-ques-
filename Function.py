# 20 Question of Functions



#Q1.Write a Python function to find the Max of three numbers.
'''Ans:def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))'''

#Q2.Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''Ans:def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) '''


#Q3.Write a Python function to check whether a number falls in a given range.
'''Ans:def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)'''

#Q4. Write a function that inputs a number and prints the multiplication table of that number?
'''Ans:def mul(num):
    """
    Prints the multipliaction table of a given number
    """
    for i in range(1, 11):
        print("{multiplier} * {multiplicand} = {multiplicantion}".format(
            multiplier=num, multiplicand=i, multiplicantion=num * i))

mul(9)
'''
#Q5.Write a function that converts a decimal number to binary number1/
'''Ans:def decToBin(num):
    """
    Prints the binary number of a given decimal number using recursion
    """
    if num > 1:
        decToBin(num//2)
    print(num % 2, end="")
        
decToBin(11)'''

#Q6.Write a program which can filter odd numbers in a list by using filter function¶
'''Ans:def filterOdd(lst):
    """
    Filter odd numbers from given list
    """
    return list(filter(lambda num: (num%2 != 0), lst))

filterOdd([0,2,5,8,19,20,34,95])'''


#Q7.Write a program which can map() to make a list whose elements are cube of elements in a given list
'''Ans:def cube(lst):
    """
    Returns the list of cubes of given number
    """
    return list(map(lambda x: x**3, lst))

cube([1, 3, 5, 9, 15])'''

#Q8.What are the 4 types of functions in Python?
'''Ans:The following are the different types of Python Functions:
Python Built-in Functions.
Python Recursion Functions.
Python Lambda Functions.
Python User-defined Functions.'''


#Q9.What does function () do in Python?
'''Ans:A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.'''

#Q10.What are the 3 functions in Python?
'''Ans:There are three functions in python that provide vast practicality and usefulness when programming. These three functions, which provide a functional programming style within the object-oriented python language, are the map(), filter(), and reduce() functions'''

#Q11.Why function is used?
'''Ans:Functions enable programmers to break down or decompose a problem into smaller chunks, each of which performs a particular task. Once a function is created, the details of how it works can almost be forgotten about'''

#Q12.How do you create a function?
'''Ans:To create a function, we must first declare it and give it a name, the same way we'd create any variable, and then we follow it by a function definition: var sayHello = function() { }; We could put any code inside that function - one statement, multiple statements - depends on what we want to do.'''

#Q13.Define a function that accepts 2 values and return its sum, subtraction and multiplication?
'''Ans:def result(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    print(f"Sum is {sum}, Sub is {sub}, & Multiply is {mul}")

a = int(input("Enter value of a: "))  # 7
b = int(input("Enter value of b: "))  # 5
result(a,b)'''

#Q14.Define a function that accepts roll number and returns whether the student is present or absent?
'''Ans:def detail(roll):
    x = [23,43,22,56]
    if roll in x:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")
roll = int(input("Enter roll no. ")) # 24
detail(roll)'''

#Q15.Define a function in python that accepts 3 values and returns the maximum of three numbers.
'''Ans:def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum among all")
    elif b > a and b > c:
        print(f"{b} is maximum among all")
    else:
        print(f"{c} is maximum among all")

max(30,22,18)'''

#Q16.Define a function that returns Factorial of a number.
'''Ans:def factorial(num):
    fact = 1
    while(num!=0):
        fact *= num
        num = num - 1
    print("Factorial is",fact)

num = int(input("Enter number "))
factorial(num)'''

#Q17.Define a function that accepts radius and returns the area of a circle.
'''Ans:def area(radius):
    area = 3.14*radius*radius
    return area

radius = int(input("Enter Radius: "))  # 4
print(area(radius))'''


#Q18.What is the scope of a variable (in function)?
'''Ans:If we are talking about scope, it means we are referring to the visibility of a variable in function. 
      If a variable is defined inside the function then it is called a local variable and its scope is limited to its own function only.'''

#Q19.What does function returns by default in Python?
'''Ans: A function should always return a value. If we do not explicitly return a value or statement 
       after the execution of a function then it returns a default value as None implicitly.'''


#Q20.Write a program to filter even and odd number from a list.
'''Ans:x = [10,23,24,35,65,78,90]
eve = []
odd = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        eve.append(x[i])
    else:
        odd.append(x[i])
print("Even numbers are: ",eve)
print("Odd numbers are: ",odd)

# output
# Even numbers are:  [10, 24, 78, 90]
# Odd numbers are:  [23, 35, 65]'''
