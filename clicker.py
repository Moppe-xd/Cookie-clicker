import turtle

skräm = turtle.Screen()
skräm.bgcolor("black")

skräm.register_shape("cookie.gif")

#Ritar cookien
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0
clicks_upgrade = 1

#Detta är för att skriva antalet kakor
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

#Detta är för att göra uppgraderingstexten
up = turtle.Turtle()
#up.hideturtle()
up.color("white")
up.penup()
up.goto(-350,100)
up.write("UPGRADE", align="center", font=("Courier New", 32, "normal"))

#Denna funktion är för att upgraderat ens klickande
def upgrade(x,y):
    global clicks
    global clicks_upgrade
    if(clicks >= 10):
        clicks_upgrade += 0.1
        clicks = round(clicks-10,3)
        pen.clear()
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

#Denna funktion är för när man klickar på cookien
def clicked(x,y):
    global clicks
    global clicks_upgrade
    clicks = round(clicks+(1*clicks_upgrade),3)
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)
up.onclick(upgrade)

skräm.mainloop()
