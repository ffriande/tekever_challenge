from flask import Flask, Blueprint

from .views import main
from .extensions import db

from .init_db import init_db

import os
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
	
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
    db.init_app(app)
    
    init_db(app)
    
    app.register_blueprint(main)
        
    return app

