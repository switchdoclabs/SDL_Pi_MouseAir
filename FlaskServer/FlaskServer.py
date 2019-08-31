from flask import Flask
import os
import logging

logging.getLogger('werkzeug').disabled = True
os.environ['WERKZEUG_RUN_MAIN'] = 'true'

try:
    os.remove("/home/pi/SDL_Pi_MouseAir/FlaskServer/static/*")
    print("Files Removed!")
except:
    pass


def threadFlask(debugValue):
    app = Flask(__name__, static_url_path='/static')

    @app.route('/')

    def index():

        return "Flask Server"

    app.run(debug=debugValue, host='0.0.0.0')


if __name__ == '__main__':

    threadFlask(True)
