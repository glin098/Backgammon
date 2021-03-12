from cs1graphics import *

response = float(input('Enter pixels per grid cell: '))
x = response

canvas = Canvas (x*3,x*2.6)
canvas.setBackgroundColor('burlywood4')

split = Path(Point(x*1.5,0), Point(x*1.5, x*2.6))
split.setBorderWidth(x*0.006)
canvas.add(split)

colors = ['tan', 'darkorange3']
colors2=['darkorange3','tan']

left = Layer()
leftRectangle = Rectangle(x*1.2, x*2.2, Point(x*0.8, x*1.3))
leftRectangle.setBorderWidth(x*0.004)
leftRectangle.setFillColor('navajowhite')
left.add(leftRectangle)

for u in range(6):
    triangle = Polygon(Point(x*0.2, x*0.2), Point(x*0.4,x*0.2), Point(x*0.3, x*1.2))
    triangle.move(x*0.2*u,0*u)
    triangle.setBorderWidth(x*0.004)
    color = colors[u%2]
    triangle.setFillColor(color)
    left.add(triangle)

for l in range(6):
    triangle2 = Polygon(Point(x*0.2,x*2.4), Point(x*0.4,x*2.4), Point(x*0.3, x*1.4))
    triangle2.move(x*0.2*l,0*l)
    triangle2.setBorderWidth(x*0.004)
    color2 = colors2[l%2]
    triangle2.setFillColor(color2)
    left.add(triangle2)
canvas.add(left)

right = left.clone()
right.move(x*1.4, 0)
canvas.add(right)
#----------numbers-------------------

bottomNum = ['1', '2', '3', '4', '5', '6',' ','7','8','9','10','11','12']


for i in range(13):
    z = bottomNum[i]
    num = Text(z, x*0.048, Point(0.3*x, 2.48*x))
    num.move(x*0.2*i,0)
    canvas.add(num)



topNum = ['24', '23', '22', '21', '20', '19',' ','18','17','16','15','14','12']
for h in range(13):
    w = topNum[h]
    num2 = Text(w, x*0.048, Point(0.3*x, 0.12*x))
    num2.move(x*0.2*h,0)
    canvas.add(num2)

#-----------checkers------------------
    
#5 checkers in a row
for num,pt,whiteOnTop in [(1.3*x,0.28*x,False),(2.7*x,0.28*x,True),(1.3*x,1.63*x,True),(2.7*x,1.63*x,False)]:
   checker=Circle(0.08*x,Point(num,pt))
   canvas.add(checker)
   if whiteOnTop==True:
       checker.setFillColor('White')
   else:
       checker.setFillColor('black')
   for numcheck in range(5):
       checker2=checker.clone()
       checker2.move(0*x*numcheck,0.17*x*numcheck)
       canvas.add(checker2)
       
#2 checkers in a row
for num,pt,whiteOnTop in [(0.3*x,0.3*x,True),(0.3*x,2.14*x,False)]:
   checker=Circle(0.08*x,Point(num,pt))
   canvas.add(checker)
   if whiteOnTop==True:
       checker.setFillColor('White')
   else:
       checker.setFillColor('black')
   for numcheck in range(2):
       checker2=checker.clone()
       checker2.move(0*x*numcheck,0.17*x*numcheck)
       canvas.add(checker2)
       
#3 checkers in a row
for num,pt,whiteOnTop in [(1.9*x,0.3*x, False),(1.9*x,1.96*x,True)]:
    checker=Circle(0.08*x,Point(num,pt))
    canvas.add(checker)
    if whiteOnTop==True:
       checker.setFillColor('White')
    else:
       checker.setFillColor('black')
    for numcheck in range(3):
       checker2=checker.clone()
       checker2.move(0*x*numcheck,0.17*x*numcheck)
       canvas.add(checker2)
