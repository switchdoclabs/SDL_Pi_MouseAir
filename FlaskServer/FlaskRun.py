from flask import Flask

def threadFlask(debugValue):
    app = Flask(__name__, static_url_path='/static')

    @app.route('/')

    def index():

        return "Flask Server"

    app.run(debug=debugValue, host='0.0.0.0')


if __name__ == '__main__':

    threadFlask(True)
