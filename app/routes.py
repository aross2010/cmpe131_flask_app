from flask import render_template, request
from flask import flash
from flask import redirect
from app import app
from app.models import Flight

def parse_departure(departure_str):
    from datetime import datetime
    return datetime.strptime(departure_str, '%H:%M:%S').timestamp()

@app.route('/')
def home():
    all_airline = [record.airline for record in Flight.query.filter().all()]
    all_airline = list(set(all_airline))

    return render_template('home.html', all_airline=all_airline)


@app.route('/results')
def results(): 

    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure = request.args.get('departure')
    return_date = request.args.get('return')
    airline = request.args.get('airline')
    price_sort = request.args.get('price_sort')
    time_sort = request.args.get('time_sort')

    departure_flights = Flight.query.filter_by(origin=origin, destination=destination, originDate=departure,airline=airline).all()
    return_flights = Flight.query.filter_by(origin=destination, destination=origin, originDate=return_date,airline=airline).all()

    paired_flight_data_list = []

    for departure_flight in departure_flights:
        for return_flight in return_flights:
            if departure_flight.airline == return_flight.airline:
                paired_flight_data = {
                    'price': departure_flight.price + return_flight.price,
                    'airline': departure_flight.airline,
                    'model': [departure_flight.model, return_flight.model],
                    'originTakeoff': departure_flight.takeoff.strftime('%H:%M:%S'),
                    'originLanding': departure_flight.landing.strftime('%H:%M:%S'),
                    'returnTakeoff': return_flight.takeoff.strftime('%H:%M:%S'),
                    'returnLanding': return_flight.landing.strftime('%H:%M:%S')
                }
                paired_flight_data_list.append(paired_flight_data)

    print(len(paired_flight_data_list))
        
    if price_sort:
        if price_sort == "price":
            paired_flight_data_list = sorted(paired_flight_data_list, key=lambda x: (x['price']))
        else:
            paired_flight_data_list = sorted(paired_flight_data_list, key=lambda x: (-x['price']))
    else:
        if time_sort == "time":
            paired_flight_data_list = sorted(paired_flight_data_list,
                                             key=lambda x: (parse_departure(x['originTakeoff'])))
        else:
            paired_flight_data_list = sorted(paired_flight_data_list,
                                             key=lambda x: (-parse_departure(x['originTakeoff'])))
    return render_template('results.html', flights=paired_flight_data_list, origin=origin, destination=destination, departure=departure, return_date=return_date)