Object Oriented Programming
Object Oriented Programming (OOP) tends to be one of the major obstacles for beginners when they are first starting to learn Python.

But no problem, As saying goes, When something is hard, it just means we have to put more time & effort.

Lets check basic GUI now for the fun part. Please try from your end.

import turtle
my_turtle = turtle.Turtle()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

Now please complete the following excercize:

With the Turtle Program: Draw a square & submit the Code.

Answer:

>>> import turtle
>>> my_turtle = turtle.Turtle()
>>> my_turtle.forward(100)
>>> my_turtle.left(90)
>>> my_turtle.forward(100)
>>> my_turtle.left(90)
>>> my_turtle.forward(100)
>>> my_turtle.left(90)
>>> my_turtle.forward(100)

Now write a script of above program & save it on the name of Turtle_game.py & run & see
the magic.

Try one more beautiful shape with following code & see the magic.

no need to understand what is abs(pos()) as of now. You will get it as you progress through.

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

Please try other shapes that you would like for more practice & submit the code for review.

Variables : Revision:

Hope you are clear & done with turtle visualization.Lets revise Variables that you already
familiar with.

Variables are very simple & it allows us to store the data.

Ex1:
naren = 'Videocon employee, belongs to hyd, works for SmartConnect'
when you run naren variable & press enter would give you following results:
>>> naren
'Videocon employee, belongs to hyd, works for SmartConnect'
Few more examples:
>>> x = 10
>>> y = 25
>>> c = 1.10
>>> x
10
>>> y
25
>>> c
1.1

Before we jump on the strings, Please go through https://trinket.io/ & let me know what is this site is all about.

Hope You are clear with Variables.
Now lets revise with strings also that you are already familiar with.

A string is usually a bit of text you want to display to someone
Python way of printing the strings:
print('Hello World')
print(naren)
print('Hi How are you doing')
print('On the way to becoming expert in oops also')

Hope You are clear with strings. Just revise Python notes for more information on strings.

Now lets revise with functions that you are already familiar with.

FUN FUN FUNCTIONS:

Lets take it from one of the above examples code & divine into two pieces:

Part#1
import turtle
my_turtle = turtle.Turtle()

Part#2: This part of the code actually draws the square.
Square#1
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

Lets say You have to make 5 times square.
So, We have to copy above program for 5times.

Square#2
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

Square#3
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

Square#4
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

Square#5
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(50)
my_turtle.forward(100)

So, Above code will draw 5sqaures. As its already getting boring as you already know these concepts.
Please use def function 7 write the program.

import turtle
my_turtle = turtle.Turtle()

def square():
     my_turtle.forward(100)
     my_turtle.left(90)
     my_turtle.forward(100)
     my_turtle.left(90)
     my_turtle.forward(100)
     my_turtle.left(90)
     my_turtle.forward(100)
    

square()
my_turtle.forward(100)
square()
my_turtle.forward(100)
square()
my_turtle.forward(100)
square()
my_turtle.forward(100)
square()
my_turtle.forward(100)

So, Finally the Functions are useful to use the same code again & again which helps us
not to write whole number of lines again & again.











