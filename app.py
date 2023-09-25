from flask import Flask, request, jsonify

app = Flask(__name__)

# Store user and driver data (simplified)
users = {}
drivers = {}

class Ride:
    def __init__(self, driver_id, user_id, destination):
        self.driver_id = driver_id
        self.user_id = user_id
        self.destination = destination

rides = []

@app.route('/register_user', methods=['POST'])
def register_user():
    user_data = request.json
    user_id = user_data['user_id']
    users[user_id] = user_data
    return jsonify({'message': 'User registered successfully'})

@app.route('/register_driver', methods=['POST'])
def register_driver():
    driver_data = request.json
    driver_id = driver_data['driver_id']
    drivers[driver_id] = driver_data
    return jsonify({'message': 'Driver registered successfully'})

@app.route('/request_ride', methods=['POST'])
def request_ride():
    ride_request = request.json
    user_id = ride_request['user_id']
    destination = ride_request['destination']

    # Find available driver (simplified)
    available_driver = list(drivers.keys())[0]

    new_ride = Ride(available_driver, user_id, destination)
    rides.append(new_ride)

    return jsonify({'message': 'Ride requested', 'driver_id': available_driver})

@app.route('/get_ride_status', methods=['GET'])
def get_ride_status():
    user_id = request.args.get('user_id')
    active_ride = None

    for ride in rides:
        if ride.user_id == user_id:
            active_ride = ride
            break

    if active_ride:
        driver_id = active_ride.driver_id
        driver_data = drivers.get(driver_id, {})
        return jsonify({'status': 'ride_in_progress', 'driver': driver_data})
    else:
        return jsonify({'status': 'no_active_ride'})

if __name__ == '__main__':
    app.run(debug=True)
