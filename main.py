from flask import Flask, request
from flask_restful import Api, Resource, abort
import time
# import pyfirmata

# Firmata setup
rele = 13
# board = pyfirmata.Arduino("/dev/ttyACM0")

app = Flask(__name__)
api = Api(app)
light_current_status = 0

def abort_by_status(light_new_status):
    global light_current_status
    if light_new_status == light_current_status:
        abort(409, message="The light is already in that state...")

class turn_light_on(Resource):
    def get(self):
        return{"Status": light_current_status}

    def put(self):
        light_new_status = request.form['status']
        abort_by_status(light_new_status)
        global light_current_status
        light_current_status= light_new_status
        # board.digital[rele].write(light_current_status)
        return light_current_status, 201

api.add_resource(turn_light_on, "/turnlight")

if __name__ == "__main__":
    app.run(debug=True)
