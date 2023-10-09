import turtle
import random
import colorgram 



obj = turtle.Turtle()

turtle.colormode(255)

colors = colorgram.extract('color.jpg', 30)
my_colors=[]

for i in colors:
	r = i.rgb.r
	g = i.rgb.g
	b = i.rgb.b	
	my_colors.append((r,g,b))
obj.penup()
obj.hideturtle()
for y in range(10):
	for x in range(10):
		obj.dot(20,random.choice(my_colors))
		obj.forward(50)
	obj.setheading(90)
	obj.forward(50)
	obj.setheading(180)
	obj.forward(500)
	obj.setheading(0)

turtle.done()