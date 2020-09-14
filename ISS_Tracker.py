import time, requests, math, turtle


def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']


    return latitude,longitude

def people_in_space(latitude,longitude):

    print('Latitude:'+ str(latitude))
    print('Longitude:'+ str(longitude))
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    amount = data['number']
    print('Number of astronauts in the ISS: ' + str(amount))
    people = data['people']

    for person in people:
        if (person['craft']=='ISS'):
            print(person['name'])

def screen(longitude,latitude):
    screen = turtle.Screen()
    screen.title('ISS Tracker')
    screen.setup(900, 446)
    screen.bgpic('mapa3.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)


    iss = turtle.Turtle()
    iss.penup()
    iss.shape('circle')
    iss.shapesize(0.3,0.3,0)
    iss.color('red')
    iss.speed(0)
    #iss.hideturtle()
    iss.setpos(float(longitude),float(latitude))
    #iss.showturtle()

    date = turtle.Turtle()
    date.hideturtle()
    date.speed(0)
    date.color('red')
    date.penup()
    date.setpos(-170,70)
    #date.write(time.ctime(), font=("Arial", 18, "normal"))

    lon = turtle.Turtle()
    lon.hideturtle()
    lon.speed(0)
    lon.color('red')
    lon.penup()
    lon.setpos(-170,-70)

    lat = turtle.Turtle()
    lat.hideturtle()
    lat.speed(0)
    lat.color('red')
    lat.penup()
    lat.setpos(-170,-80)

    while True:
        latitude,longitude = get_iss_position()
        
        iss.setpos(float(longitude),float(latitude))
        lat.speed(0)
        lon.speed(0)

        #date.penup()
        date.write(time.ctime(), font=("Arial", 18, "normal"))
        lat.write('Latitude:'+ latitude , font=("Arial", 16, "normal"))
        lon.write('Longitude:'+ longitude , font=("Arial", 16, "normal"))
        time.sleep(5)
        lat.clear()
        lon.clear()
        date.clear()





def main():
    lati,long= get_iss_position()
    people_in_space(lati,long)
    screen(long,lati)

main()
