from .models import Customer
from .extensions import db


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    
        customer1 = Customer(name='Francisco', surname='Friande')
        customer2 = Customer(name='Pedro', surname='Soares')
        customer3 = Customer(name='Francisca', surname='Silva')
        customer4 = Customer(name='Joana', surname='Costa')

        db.session.add_all([ customer1,  customer2,  customer3, customer4])

        db.session.commit()