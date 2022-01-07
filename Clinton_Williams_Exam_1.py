#   Exam 1 Assignment 
#   Author: Clinton Williams

#   -------
#   Part 1:
#   -------

#1.  b) iteration
#2.  c) Smaller instances of the same problem
#3.  c) Base case
#4.  a) Program gets into an infinite loop
#5.  c) Recursion uses more memory compared to iteration
#6.  c) Stack
#7.  c) Repeat a piece of code until a condition is false
#8.  c) #
#9.  b) May have no parameters
#10. b) False

#   -------
#   Part 2: Code Review
#   -------

# Yes, there is something wrong with the code. There is no end to the recursive loop. No base case.
#   -------
#   Part 3: Iterative Function
#   -------

def func1(n):
    reverselist=[]
    for i in range(len(n)-1,-1,-1):
        reverselist.append(n[i])
    return reverselist

L1=[1,2,3,4,5,6]
L2=func1(L1)
print(L2)

#   -------
#   Part 4: Recursive Function
#   -------
def func2(n):
    if len(n)==0:
        return []
    else:
        return[n.pop()]+func2(n)
      
L1=[1,2,3,4,5,6]
L2=func2(L1)
print(L2)
