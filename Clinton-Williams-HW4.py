#   HW4 Assignment 
#   Author: Clinton Williams

from matplotlib.lines import lineStyles

#   -------
#   Part 1: Point
#   -------

import numpy as np
import matplotlib.pyplot as plt
from numpy import multiply

t=np.arange(0,5*np.pi,0.01)
x=t*np.cos(t)
y=t*np.sin(t)


plt.plot(x,y,
         color='g')
plt.title("Part 1: Archimedean Spiral")
plt.xlabel("X")
plt.ylabel("Y")
#plt.show()

#   -------
#   Part 2: Heart
#   -------
t=np.arange(0,2*np.pi,0.01)
x=16*np.sin(t)**3
y=13*np.cos(t)-5*np.cos(2*t)-2.5*np.cos(3*t)-np.cos(4*t)

plt.plot(x,y,
         linestyle='--',
         color='r')
plt.title("Part 2: Heart")
plt.xlabel("X")
plt.ylabel("Y")
#plt.show()

#   -------
#   Part 3: Graphs
#   -------
print("Part 3: Graphs")

#The vertices are the chemical products, P1 through Pk,
#and the edges are connecting the products that can be shipped together.
#For example, since Pi is not compatible with Pi=1, all the odd numbered
#vertices will be connected by an edge and all except Pk, and all the even
#numbered vertices will be connected by an edge.
#So, if you have an even amount of product, you will need two trucks and three
#trucks if you have an odd number of products.

#Algorithm
def Mintrucks(k):
    if k==0:
        return 0;
    elif k==1:
        return 1;
    elif k%2==0:
        return 2;
    else:
        return 3;
print("The number of trucks needed are {}.".format(Mintrucks(21)))
print('\n')

#Trying to graph
class Graph:
    def __init__(self,n):
        self.n=n
        self.edges=self.buildMatrix()
        
    def buildMatrix(self):
        res=[]
        for i in range(0,self.n):
            col=[]
            for j in range(0,self.n):
                col.append(0)
            res.append(col)
        return res
    
    def toString(self):
        s=''
        for e in self.edges:
            s+=str(e)+'\n'
        return s

    def addEdge(self,i,j):
        try:
            self.edges[i][j]=1
        except IndexError:
            print('Could not add edge ({},{})'.format(i,j))
            print('Index error')
    
class Test:
    def test1():
        g=Graph(4)
        print(g.toString())
        
#   -------
#   Part 4: Algorithm
#   -------
print('\n')
print('Part 4: Algorithm')

def EgyptianAlgorithm(x,y):
    if y==0:
         return x
    elif y%2==0:
        print(y)
        return 2*EgyptianAlgorithm(x,y//2)
    else:
        print(y)
        return x+EgyptianAlgorithm(x,y//2)
 

print(EgyptianAlgorithm(7, 10)) 
