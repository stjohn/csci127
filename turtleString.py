#Modified by:  Jacob Kong
#Email:      jacob.kong53@myhunter.cuny.edu
#A program that uses command strings to control turtle drawing


import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'B':          #go backwards
        tess.backward(50)
    elif ch == 'g':          #turn green
        tess.color("green")
    elif ch == 'b':          #turn blue
        tess.color("blue")
    elif ch == 'S':          #stamp
        tess.stamp()
    elif ch == 'l':          #left 45
        tess.left(45)
    elif ch == 'r':          #right 45
        tess.right(45)
    elif ch == 'p':          #purple
        tess.color("purple")
    else:                   #for any other character, print an error message
        print("Error: do not know the command:", c)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked
