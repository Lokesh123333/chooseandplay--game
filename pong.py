import turtle

l=turtle.Screen()
l.title("Pong")
l.bgcolor("black")
l.setup(width=800,height=600)
l.tracer(0)
l.bgcolor("red")

#side1
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("blue")
pad_a.penup()
pad_a.goto(-350,0)
pad_a.shapesize(stretch_wid=5,stretch_len=1)



#side2
pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("blue")
pad_b.penup()
pad_b.goto(350,0)
pad_b.shapesize(stretch_wid=5,stretch_len=1)


#pingpong
pingpong=turtle.Turtle()
pingpong.speed(0)
pingpong.shape("square" )
pingpong.color("white")
pingpong.penup()
pingpong.goto(0,0)
pingpong.dx = 0.2
pingpong.dy = 0.2

#pen
lok=turtle.Turtle()
lok.speed(0)
lok.color("black")
lok.penup()
lok.hideturtle()
lok.goto(0,260)
lok.write("Player A: 0  |  Player B : 0", align="center", font=("Courier",24,"normal")  )



score_a=0
score_b=0
game_started= False

def move_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)
def move_b_down():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)
    
def move_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)
def move_a_down():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)
    
def start_game():
    global game_started
    game_started = True

l.listen()
l.onkey(move_a_up,"q")
l.onkey(move_a_down,"z")
l.onkey(move_b_up,"Up")
l.onkey(move_b_down,"Down")
l.onkeypress(start_game)
 
#main loop
while True:
  if game_started:
    
#movement
    pingpong.setx(pingpong.xcor() + pingpong.dx) 
    pingpong.sety(pingpong.ycor() + pingpong.dy)
    
#border check
    if pingpong.ycor()>290:
        pingpong.sety(290)
        pingpong.dy *= -1
    
    elif pingpong.ycor() < -290:
        pingpong.sety(-290)
        pingpong.dy *= -1
    
    if pingpong.xcor() > 350:
       pingpong.goto(0,0)
       pingpong.dx *= -1
       score_a +=1
       lok.clear()
       lok.write("Player A: {}  |  Player B : {}".format(score_a,score_b), align="center", font=("Courier",24,"normal")  )
       
    elif pingpong.xcor() < -350:
       pingpong.goto(0,0)
       pingpong.dx *= -1
       score_b += 1
       lok.clear()
       lok.write("Player A: {}  |  Player B : {}".format(score_a,score_b), align="center", font=("Courier",24,"normal")  )
       
       
    if (pingpong.xcor()>340 and pingpong.xcor()< 350) and (pingpong.ycor() < pad_b.ycor() + 40 and pingpong.ycor()>pad_b.ycor() -40):
         pingpong.setx(340)
         pingpong.dx *= -1
     
    elif (pingpong.xcor()<-340 and pingpong.xcor()> -350) and (pingpong.ycor() < pad_a.ycor() + 40 and pingpong.ycor()>pad_a.ycor() -40):
         pingpong.setx(-340)
         pingpong.dx *= -1
         
# border check for side1 paddle
    if pad_a.ycor() > 250:
        pad_a.sety(250)
    elif pad_a.ycor() < -240:
        pad_a.sety(-240)

# border check for side2 paddle
    if pad_b.ycor() > 250:
        pad_b.sety(250)
    elif pad_b.ycor() < -240:
        pad_b.sety(-240)
  else:
        lok.clear()
        lok.write("Press any key to start the game", align="center", font=("Courier", 24, "normal"))
  try:
        l.update()
  except turtle.Terminator:
        break 