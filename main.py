import turtle
screen = turtle.Screen()

def Piece_Movements():
   tb1 = turtle.Turtle() 
   tb1.penup() #I don't want my pieces to ever draw anything
   tb1.fillcolor('black')#These are my black pieces
   tb1.shapesize(3.0, 3.0, 3.0)#Making it a good size
   tb1.shape("circle")
   tb2 = tb1.clone() #using clone() means that I don't have to write the same code for each turtle
   tb3 = tb1.clone()
   tb4 = tb1.clone()
   tw1 = turtle.Turtle()
   tw1.penup()
   tw1.fillcolor('white')
   tw1.shapesize(3.0, 3.0, 3.0)
   tw1.shape("circle")
   tw2 = tw1.clone() 
   tw3 = tw1.clone()
   tw4 = tw1.clone()
   theBoard = {'1': (-120.71,29.29) , '2': (-50,100) ,
             '3': (50,100) ,'4': (120.71,29.29) , 
             '5': (120.71,-70.71) , '6': (50.00,-141.42) ,
             '7': (-50.00,-141.42) , '8': (-120.71,-70.71) ,'9': (0,-15)}
    #The 9 places on the board. 
   tb1.goto(theBoard['1'])
   tb2.goto(theBoard['2'])
   tb3.goto(theBoard['3'])
   tb4.goto(theBoard['4'])
   tw1.goto(theBoard['5'])
   tw2.goto(theBoard['6'])
   tw3.goto(theBoard['7'])
   tw4.goto(theBoard['8'])
   tb1.ondrag(tb1.goto)
   tb2.ondrag(tb2.goto)
   tb3.ondrag(tb3.goto)
   tb4.ondrag(tb4.goto)
   tw1.ondrag(tw1.goto)
   tw2.ondrag(tw2.goto)
   tw3.ondrag(tw3.goto)
   tw4.ondrag(tw4.goto)
Piece_Movements()

