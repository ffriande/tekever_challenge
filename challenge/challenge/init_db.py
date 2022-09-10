from .models import Customer, Account, Transaction
from .extensions import db


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    
        customer1 = Customer(name='Francisco', surname='Friande')
        customer2 = Customer(name='Pedro', surname='Soares')
        customer3 = Customer(name='Francisca', surname='Silva')
        customer4 = Customer(name='Joana', surname='Costa')
    
        transaction1 = Transaction(value=0)
        transaction2 = Transaction(value=0)
        transaction3 = Transaction(value=10)
        transaction4 = Transaction(value=10)

        account1 = Account(balance=0, transactions=[transaction1], customer_id=1)
        account2 = Account(balance=0, transactions=[transaction2], customer_id=2)
        account3 = Account(balance=10, transactions=[transaction3], customer_id=3)
        account4 = Account(balance=10, transactions=[transaction4], customer_id=4)
    
        db.session.add_all([ customer1,  customer2,  customer3, customer4])
        db.session.add_all([ transaction1,  transaction2,  transaction3, transaction4])
        db.session.add_all([ account1,  account2,  account3, account4])

        db.session.commit()