import turtle

skärm = turtle.Screen()
skärm.bgcolor("black")
skärm.title("Cookie Clicker")

skärm.register_shape("cookie.gif")

#Ritar cookien
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0
clicks_upgrade = 1
clicks_auto = 0
running  = True

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
up.write("UPGRADE costs: 10", align="center", font=("Courier New", 32, "normal"))

#Skriver texten för automatisk klickning
auto = turtle.Turtle()
auto.color("white")
auto.penup()
auto.goto(350,100)
auto.write("Auto costs: 10", align="center", font=("Courier New", 32, "normal"))

#Updaterar mängden kakor man har
def skriv_cookie():
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))


#Denna funktion är för att upgraderat ens klickande
def upgrade(x,y):
    global clicks, clicks_upgrade
    if(clicks >= 10 * clicks_upgrade):
        clicks = round(clicks-(10 * clicks_upgrade),3)
        clicks_upgrade += 1
        temp = round(10 * clicks_upgrade)
        up.clear()
        skriv_cookie()
        up.write(f"UPGRADE costs: {temp}", align="center", font=("Courier New", 32, "normal"))

#Denna funktion är för när man klickar på cookien
def clicked(x,y):
    global clicks, clicks_upgrade
    clicks = round(clicks+(1*clicks_upgrade),3)
    skriv_cookie()

#Upgraderar auto klickadet
def auto_upgrade(x,y):
    global clicks, clicks_auto
    if (clicks >= 10 + (10 * clicks_auto)):
        clicks = round(clicks-(10 + (10 * clicks_auto)),3)
        clicks_auto += 0.1
        temp = round((10 + (10 * clicks_auto)),3)
        skriv_cookie()
        auto.clear()
        auto.write(f"Auto costs: {temp}", align="center", font=("Courier New", 32, "normal"))

    
#Denna funktion generar kakor varje sekund
def auto_click():
    global clicks, clicks_auto
    clicks = round(clicks+(1*clicks_auto),3)
    skriv_cookie()
    skärm.ontimer(auto_click,1000)


cookie.onclick(clicked)
up.onclick(upgrade)
auto.onclick(auto_upgrade)
skärm.ontimer(auto_click,1000)

skärm.mainloop()
