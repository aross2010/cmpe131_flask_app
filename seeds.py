import datetime
import random
from app import db, app
from app.models import Flight


def generateFlights():
    airports = ['NYC', 'SFO', 'LAX', 'ORD', 'MIA', 'DFW']
    models = ['Boeing 747', 'Airbus A320', 'Boeing 777']
    airlines = ['Delta', 'United', 'JetBlue', 'Southwest']

    flights = []
    for _ in range(1000):
        origin = random.choice(airports)
        destination = random.choice([a for a in airports if a != origin])
        
        takeoff = datetime.datetime(2024, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59))
        landing = takeoff + datetime.timedelta(hours=random.randint(1, 6), minutes=random.randint(0, 59))
        
        model = random.choice(models)
        airline = random.choice(airlines)
        
        price = round(random.uniform(250, 800), 2)
        
        flight = Flight(origin=origin, destination=destination, takeoff=takeoff, landing=landing, date=takeoff.date(), model=model, airline=airline, price=price)
        flights.append(flight)
    
    return flights

 # generate 1000 random flights

def main():
  
    with app.app_context():

        db.create_all()

       
        flights = generateFlights()
        
        
        for flight in flights:
            db.session.add(flight)
        
        
        db.session.commit()

if __name__ == '__main__':
    main()