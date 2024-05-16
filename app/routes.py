from flask import render_template, request
from flask import flash
from flask import redirect
from app import app
from app.models import Flight


@app.route('/')
def home():
    discounted_flights = Flight.query.filter(Flight.price < 150).limit(10).all()
    return render_template('home.html', discounted_flights=discounted_flights)

@app.route('/results')
def results(): 

    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure = request.args.get('departure')
    return_date = request.args.get('return')
    
    departure_flights = Flight.query.filter_by(origin=origin, destination=destination, originDate=departure).all()
    return_flights = Flight.query.filter_by(origin=destination, destination=origin, originDate=return_date).all()

    departure_flights_data = [flight.__dict__ for flight in departure_flights]
    return_flights_data = [flight.__dict__ for flight in return_flights]

    paired_flight_data_list = []


    for departure_flight in departure_flights:
        for return_flight in return_flights:
            if departure_flight.airline == return_flight.airline:
                paired_flight_data = {
                    'price': departure_flight.price + return_flight.price,
                    'airline': departure_flight.airline,
                    'model': [departure_flight.model, return_flight.model],
                    'class_type': departure_flight.class_type, # added class_type ===========================================
                    'originTakeoff': departure_flight.takeoff.strftime('%H:%M:%S'),
                    'originLanding': departure_flight.landing.strftime('%H:%M:%S'),
                    'returnTakeoff': return_flight.takeoff.strftime('%H:%M:%S'),
                    'returnLanding': return_flight.landing.strftime('%H:%M:%S')
                }
                paired_flight_data_list.append(paired_flight_data)

    print(len(paired_flight_data_list))
        

    return render_template('results.html', flights=paired_flight_data_list, origin=origin, destination=destination, departure=departure, return_date=return_date)

