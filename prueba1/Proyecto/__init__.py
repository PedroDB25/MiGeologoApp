import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')
    return app

        @app.route('/pro1')
    def index():
        return render_template('pro1.html')
    return app
        @app.route('/pro2')
    def index():
        return render_template('error.html')
    return app
        @app.route('/pro3')
    def index():
        return render_template('error.html')
    return app
        @app.route('/pro4')
    def index():
        return render_template('error.html')
    return app
        @app.route('/pro5')
    def index():
        return render_template('error.html')
    return app
        @app.route('/pro6')
    def index():
        return render_template('error.html')
    return app