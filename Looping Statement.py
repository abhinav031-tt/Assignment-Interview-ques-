# 20 Question of Looping Statement

#Q1.Which of the following type of loop(s) is/are not supported by Python?
'''Ans:  do while    '''

#Q2.What would be the result of executing the following code?
#n = sum(range(2,4))
#while n:
 #   print(n, end = ' ')
  #  n = n - 1
  #  break
 ##   print('End', end = ' ')
'''Ans:The output is 5  '''

#Q3.Which statement is used inside a loop to skip the rest of the code for the current iteration, so execution can continue with the next iteration?
'''Ans:  Continue'''

#Q3.Which Python statement is used to bring control out of the current loop?
'''Ans: The break Statement  '''

#Q4.What would be the result of executing the following code?
#sum = 0
#for i in range(5, 0, -2):
 #   sum += i > sum
#print(sum)
'''Ans: The Output is 2 '''

#Q5.Which of the following code will result in an infinite loop?Which of the following code will result in an infinite loop?
'''Ans: while(-1):
    print ('OK')'''

#Q6.How does For loop and While loop differ in Python and when do you choose to use them?
'''Ans:For loop is generally used to iterate through the elements of various collection types such as List, Tuple, Set, and Dictionary.
       While loop is the actual looping feature that is used in any other programming language. This is how Python differs in handling loops from the other programming languages.  '''


#Q7. What is the difference between a for loop and a while loop?
'''Ans:A for loop is typically used when you know exactly how many times the loop needs to be repeated. A while loop is typically used when you don't know how many times the loop needs to be repeated.
       A while loop repeats as long as its condition is true. For example, if a while loop says "while x == 5", then the line will execute as long as x equals five.'''


#Q8.What is the Python syntax for a for loop?
'''Ans:The for loop is a programming construct that allows you to iterate over an arbitrary range of values, mapping them to the required actions.
        It can be thought of as an extension of the mathematical notion of a for loop, which is defined as "a control structure that enables one to iterate (repeat) a process (such as counting or summing) while varying the process's start value (or its end point), step size, and/or direction."  '''


#Q9. What are the advantages of using a for loop in Python?
'''Ans:A for loop is a type of loop that executes a set of instructions repeatedly. It uses the following syntax: for x in range(y): do something'''

#Q10.What is the syntax for Python For loop ?
'''Ans:for variable in sequence:
      statement1
      statement2
      statementN
    for is keyword
    sequence can be a list, string, typle or rance
    for ith iteration, the ith element of sequence is loaded to variable
    statements has to written with indentation'''


#Q11.What is the output of the following?
#x = "abcdef"
#i = "a"
#while i in x:
#    x = x[:-1]
#    print(i, end = " ")
'''Ans: The output is a a a a a a '''

#Q13.What is the output of the following?
#x = "abcdef"
#i = "i"
#while i in x:
#    print(i, end=" ")
'''Ans: No output  '''

#Q14.What is the output of the following?
#x = 'abcd'
#or i in range(len(x)):
#    x[i].upper()
#print (x)
'''Ans: The output is abcd'''




#Q15.Which of the following is True regarding loops in Python?
'''Ans: Keyword "break" can be used to bring control out of the current loop.'''


#Q16. Which of the following Python code will give different output from the others?
'''Ans:for k in [0,1,2,3,4,5]:
    print(k)'''

#Q17.How many times will the loop run?
#i=2
#while(i>0):
#   i=i-1
'''Ans:The Output is 2'''



#Q18.Which of the following is a valid for loop in Python?
'''Ans:for i in range(0,5):'''

#Q19.When does the else statement written after loop executes?
'''Ans: When loop condition becomes false'''

#Q20. What will be the output of the following code?
#x = "abcdef"
#i = "i"
#while i in x:
#   print(i, end=" ")

'''Ans:No output'''
