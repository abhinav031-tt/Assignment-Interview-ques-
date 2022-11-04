# 20 Question of Conditional Statement


#Q1.Which of the following if statements is a good candidate for using a ternary operator instead?
'''Ans:
if condition_a
  something
else
  something_else
end
'''

#Q2.Let's convert the correct answer above using a ternary operator. Which of the following is the correct way to do that?
'''Ans:condition_a ? something : something_else'''

#Q3.When is it a good idea to use an if conditional over a ternary?
'''Ans:When the if statement is complex with multiple elseif conditions
       When it would require a nested ternary statement
       When the ternary statement takes up more than one line'''


#Q4: name = "Steven"
#puts "Hi, #{name}" if name == "Steven"     
'''Ans:  "Hi, Steven"   '''


#Q5:If you are unsure whether to use the ternary operator, or the if statement, which should you use?

'''Ans:if statement   '''

#Q6.How are if, elif, and else blocks defined?
'''Answer:All blocks in Python are defined by indenting. All lines of a particular code block must have the same level of indenting.'''

#Q7.How is the Python switch statement used?
'''Ans:This is a trick question, there is no built-in switch statement in Python, which is unusual. A switch statement can be easily created using if-elif using lambda or with Python dictionaries.'''

#Q8. What are the 3 types of Python conditional statements?
'''Ans:if statements.
      if-else statements.
      elif statements.
      Nested if and if-else statements.
      elif ladder.
'''
#Q9.num = 5
#if(num > 10):
 #    print(“number is greater than 10”)
#else:
#     print(“number is less than 10”)
 
#print (“This statement will always be executed” )
'''Ans:  Number is less than 10.    '''

#Q10.What are the conditional statements used in Python?
'''Ans:Equals: a == b.
Not Equals: a != b.
Less than: a < b.
Less than or equal to: a <= b.
Greater than: a > b.
Greater than or equal to: a >= b.
'''

#Q11.How do you reduce if-else in Python?
'''Ans:Use If/Else Statements in One Line To simplify the code and reduce the number of lines in the conditional statements, you can use an inline if conditional statement'''

#Q12.In a Python program, a control structure?
'''Ans:Directs the order of execution of the statements in the program.if, if/else, and if/elif/else statements are all examples of control structures '''

#Q13.Which one of the following if statements will not execute successfully?
'''Ans:if (1, 2):
    print('foo')'''

#Q14.    if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
   # print(1)
    #print(2)
    #if 'a' in 'qux':
     #   print(3)
#print(4)

'''Ans:The Output is 1,2,4'''

#Q15 Write a Python if/else statement to assign the smaller of a and b to the variable m. wheras a = 100 and b= 50
'''Ans:if a < b:
    m = a
 else:
    m = b'''

#Q16.Is while a conditional statement in Python?
'''Ans:The flow of execution for a while statement works like this:
      Evaluate the condition ( BOOLEAN EXPRESSION ), yielding False or True .
     If the condition is false, exit the while statement and continue execution at the next statement.'''


#Q17. When Should You Use The “Break” In Python? 
'''Ans:Python provides a break statement to exit from a loop. Whenever the break hits in the code, the control of the program immediately exits from the body of the loop.'''


#Q18.What is the use of Nested If-Else Statement?

'''Ans:It is a conditional statement which is used when we want to check more than 1 condition at a time in a same program. The conditions are executed from top to bottom checking each condition whether it meets the conditional criteria or not. If it found the condition is true then it 
       executes the block of associated statements of true part else it goes to next condition to execute.'''


#Q19. What are the advantages of switch case?
'''Ans: It is easy to use.
• It is easy to find out errors.
• Debugging is made easy in switch case.
• Complexity of a program is minimized.'''     

#Q20.What comes first in a conditional statement?
'''Ans:A conditional statement includes two main components: a hypothesis and a conclusion. The hypothesis establishes a basis against which you can compare your conclusion. In a basic conditional statement, the hypothesis comes first, and the conclusion comes second.'''
