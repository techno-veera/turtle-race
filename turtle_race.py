from turtle import *
import random as rn
import time

bgcolor("black")
speed(0.01)

ta=Turtle()
ta.hideturtle()
ta.penup()
ta.color("white")
ta.goto(-100,370)
ta.write("TURTLE RACE")
time.sleep(1)
ta.reset()

t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
t5=Turtle()
t6=Turtle()
t7=Turtle()
t8=Turtle()
t9=Turtle()
t10=Turtle()
t11=Turtle()
t12=Turtle()

t13=Turtle()



t1.shape("turtle")
t1.shapesize(2,2,1)
t1.color("red")
t1.penup()
t1.goto(-200,370)
t1.pendown()
t1.right(90)

t2.shape("turtle")
t2.shapesize(2,2,1)
t2.color("blue")
t2.penup()
t2.goto(-160,370)
t2.pendown()
t2.right(90)

t3.shape("turtle")
t3.shapesize(2,2,1)
t3.color("green")
t3.penup()
t3.goto(-120,370)
t3.pendown()
t3.right(90)

t4.shape("turtle")
t4.shapesize(2,2,1)
t4.color("cyan")
t4.penup()
t4.goto(-80,370)
t4.pendown()
t4.right(90)

t5.shape("turtle")
t5.shapesize(2,2,1)
t5.color("yellow")
t5.penup()
t5.goto(-40,370)
t5.pendown()
t5.right(90)

t6.shape("turtle")
t6.shapesize(2,2,1)
t6.color("pink")
t6.penup()
t6.goto(0,370)
t6.pendown()
t6.right(90)

t7.shape("turtle")
t7.shapesize(2,2,1)
t7.color("white")
t7.penup()
t7.goto(40,370)
t7.pendown()
t7.right(90)

t8.shape("turtle")
t8.shapesize(2,2,1)
t8.color("gold")
t8.penup()
t8.goto(80,370)
t8.pendown()
t8.right(90)

t9.shape("turtle")
t9.shapesize(2,2,1)
t9.color("orange")
t9.penup()
t9.goto(120,370)
t9.pendown()
t9.right(90)

t10.shape("turtle")
t10.shapesize(2,2,1)
t10.color("skyblue")
t10.penup()
t10.goto(160,370)
t10.pendown()
t10.right(90)

t11.shape("turtle")
t11.shapesize(2,2,1)
t11.color("purple")
t11.penup()
t11.goto(200,370)
t11.pendown()
t11.right(90)

t12.hideturtle()
t12.color("white")
t12.penup()
t12.goto(-230,337)
t12.pendown()
t12.forward(455)

t12.hideturtle()
t12.color("white")
t12.penup()
t12.goto(-230,-360)
t12.pendown()
t12.forward(455)



t13.hideturtle()
t13.color("white")
t13.goto(-20,0)
t13.write("START")

time.sleep(1)
t13.reset()

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0
n10=0
n11=0

red=0
for I in range(1,90):
	
	r1=rn.randint(1,20)
	t1.forward(r1)
	p1=t1.position()
	n1=n1+r1
	
	r2=rn.randint(1,20)
	t2.forward(r2)
	p2=t2.position()
	n2=r2+n2
	
	r3=rn.randint(1,20)
	t3.forward(r3)
	p3=t3.position()
	n3=r3+n3
	
	r4=rn.randint(1,20)
	t4.forward(r4)
	p4=t4.position()
	n4=r4+n4
	
	r5=rn.randint(1,20)
	t5.forward(r5)
	p5=t5.position()
	n5=r5+n5
	
	r6=rn.randint(1,20)
	t6.forward(r6)
	p6=t6.position()
	n6=r6+n6
	
	r7=rn.randint(1,20)
	t7.forward(r7)
	p7=t7.position()
	n7=r7+n7
	
	r8=rn.randint(1,20)
	t8.forward(r8)
	p8=t8.position()
	n8=r8+n8
	
	r9=rn.randint(1,20)
	t9.forward(r9)
	p9=t9.position()
	n9=r9+n9
	
	r10=rn.randint(1,20)
	t10.forward(r10)
	p10=t10.position()
	n10=r10+n10
	
	r11=rn.randint(1,20)
	t11.forward(r11)
	p11=t11.position()
	n11=r11+n11




t1.reset()
t2.reset()
t3.reset()
t4.reset()
t5.reset()
t6.reset()
t7.reset()
t8.reset()
t9.reset()
t10.reset()
t11.reset()
	
tb=Turtle()
tb.hideturtle()
tb.penup()
tb.color("yellow")
tb.goto(-100,0)
tb.write("TURTLE RACE FINISH")
time.sleep(1)

with open("turtle.txt","w") as tr:
	tr.write("red={}\n blue={}\n green={}\n cyan={}\n yellow={}\n pink={}\n white={}\n gold={}\n orange={}\n skyblue={}\n purple={}\n".format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11))

exitonclick()