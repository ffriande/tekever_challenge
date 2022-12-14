from .extensions import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    transactions = db.relationship('Transaction', backref='account')
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    
    def __repr__(self):
        return f'<Account id={self.id} balance={self.balance} transactions={self.transactions} customer_id={self.customer_id}>'
    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    accounts = db.relationship('Account', backref='customer')
    
    def __repr__(self):
        return f'<Customer {self.name} {self.surname}; id={self.id}>'
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)     
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __repr__(self):
        return f'<Transaction to acc_id={self.account_id}, with value={self.value}EUR; id={self.id}>'