from flask import Flask
from project.routes.route import blueprint

class App:  # Class for creating the app
    def __init__(self, name, template_folder, static_folder):  # Initializing the app
        self.name = name
        self.template_folder = template_folder
        self.static_folder = static_folder

    def create_app(self):  # Creating the app
        app = Flask(self.name, template_folder=self.template_folder, static_folder=self.static_folder)
        app.register_blueprint(blueprint, url_prefix='/')
        return app

    def run_app(self, app, host, port, debug):  # Running the app
        app.run(host=host, port=port, debug=debug)