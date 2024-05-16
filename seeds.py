import datetime
import random
from app import db, app
from app.models import Flight


airport_distances = {
    ('JFK', 'SFO'): 6,
    ('JFK', 'LAX'): 7,
    ('JFK', 'ORD'): 3,
    ('JFK', 'MIA'): 3,
    ('JFK', 'DFW'): 3,
    ('SFO', 'JFK'): 6,  # Added route from SFO to JFK
    ('SFO', 'LAX'): 1,
    ('SFO', 'ORD'): 4,
    ('SFO', 'MIA'): 5,
    ('SFO', 'DFW'): 4,
    ('LAX', 'JFK'): 7,  # Added route from LAX to JFK
    ('LAX', 'SFO'): 1,
    ('LAX', 'ORD'): 4,
    ('LAX', 'MIA'): 5,
    ('LAX', 'DFW'): 3,
    ('ORD', 'JFK'): 3,  # Added route from ORD to JFK
    ('ORD', 'SFO'): 4,
    ('ORD', 'LAX'): 4,
    ('ORD', 'MIA'): 3,
    ('ORD', 'DFW'): 2,
    ('MIA', 'JFK'): 3,  # Added route from MIA to JFK
    ('MIA', 'SFO'): 5,
    ('MIA', 'LAX'): 5,
    ('MIA', 'ORD'): 3,
    ('MIA', 'DFW'): 2,
    ('DFW', 'JFK'): 3,  # Added route from DFW to JFK
    ('DFW', 'SFO'): 4,
    ('DFW', 'LAX'): 3,
    ('DFW', 'ORD'): 2,
    ('DFW', 'MIA'): 2,
}

# generate 10,000 random flights
def generateFlights():
    models = ['Boeing 747', 'Airbus A320', 'Boeing 777']
    airlines = ['Delta', 'United', 'JetBlue', 'Southwest']

    # clear existing flights
    Flight.query.delete()

    flights = []
    for _ in range(20000):
        origin, destination = random.choice(list(airport_distances.keys()))
        distance = airport_distances[(origin, destination)]
        
        takeoff = datetime.datetime(2024, 12, random.randint(1, 28), random.randint(0, 23), random.randint(0, 59))
        landing = takeoff + datetime.timedelta(hours=distance)
        
        origin_date = takeoff.date()
        destination_date = landing.date() if landing.date() != origin_date else landing.date() + datetime.timedelta(days=1)
        
        model = random.choice(models)
        airline = random.choice(airlines)
        
        price = random.randint(100, 500)
        
        flight = Flight(origin=origin, destination=destination,
                        takeoff=takeoff, landing=landing,
                        originDate=origin_date, destinationDate=destination_date,
                        model=model, airline=airline, price=price)
        flights.append(flight)
    
    return flights

def main():
  
    with app.app_context():
        db.drop_all()
        db.create_all()

        flights = generateFlights()
        
        
        for flight in flights:
            db.session.add(flight)
        
        
        db.session.commit()

if __name__ == '__main__':
    main()

# JFK -> LAX 12-12 to 12-22