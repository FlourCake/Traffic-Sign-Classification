from flask import Flask
from routes.route import blueprint

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')  # flask app object
    return app

app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)