---------------------------------------
Authors: grace.lin@slu.edu, lili.hostetler@slu.edu

---------------------------------------
Approximate number of hours spent: 
3-4
---------------------------------------
Citation of any help received from (approved) sources:
Professor Holdener
---------------------------------------
Brief overview of program, including any known bugs:
The program is a backgammon board where the user can input the size in pixels
of how big they want their backgammon board to be. We implemented maintaining a "size" variable
so that the program can draw the size of the board at whatever scale the user inputs.
---------------------------------------
Other comments or response program-specific questions:
We tried to reduce the number of for loops within the program regarding the checkers, 
the number of checkers, and the position of the checkers. The error that we couldnt seem to 
fix is "'list' object cannot be interpreted as an integer." 

This is the code that we had:

listLoops = [2,3,5]
listLoops = list(map(int, listLoops))

for num,pt,whiteOnTop in [(1.3*x,0.28*x,False),(2.7*x,0.28*x,True),(1.3*x,1.63*x,True),(2.7*x,1.63*x,False),(1.9*x,0.3*x, False),(1.9*x,1.96*x,True),(0.3*x,0.3*x,True),(0.3*x,2.14*x,False),(1.9*x,0.3*x, False),(1.9*x,1.96*x,True)]:
   checker=Circle(0.08*x,Point(num,pt))
   canvas.add(checker)
   if whiteOnTop==True:
       checker.setFillColor('White')
   else:
       checker.setFillColor('black')
       
   for numcheck in range(listLoops):
       for numcheck,pos in [(2,0.3*x,0.3*x), (3, 1.9*x,0.3*x), (5, 2.7*x, 0.3*x)]:
           checker2=checker.clone()
           checker2.move(0*x*pos,0.17*x*pos)
           canvas.add(checker2)
---------------------------------------