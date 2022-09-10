from flask import Blueprint, request
from .extensions import db
from .models import Customer, Account, Transaction
import json 
main = Blueprint('main', __name__)

    
@main.route('/')
def index():
    return 'Hello World!'


@main.route('/create_account', methods=['POST'])
def create_account():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json)

        if not ('customerID' in json and 'initialCredit' in json):
            return 'Payload fields incorrect'

        balance = json['initialCredit']
        transactions = []
        
        if balance != 0:
            t = Transaction(value=balance)
            transactions.append(t)
            db.session.add(t)
        
        new_account = Account(balance=balance, transactions=transactions, customer_id=json['customerID'])
        db.session.add(new_account)
        
        db.session.commit()
        
        return json
    else:
        return 'Content-Type not supported!'
    return 

@main.route('/user_info', methods=['GET'])
def user_info():
    
    args = request.args
    
    if 'customerID' not in args:
        return 'Parameters fields are incorrect!'    
            
    customer = Customer.query.get(args['customerID'])
    
    balance = 0
    transactions = []
    
    for acc in customer.accounts:
        balance += acc.balance
        for trans in acc.transactions:
            transactions.append(str(trans))
    
    return json.dumps({'name': customer.name, 'surname': customer.surname, 'balance': balance, 'accounts_transactions':transactions})
    return 


@main.route('/dump_db', methods=['GET'])
def dump_db():
    custs = Customer.query.all()
    trans = Transaction.query.all()
    accs = Account.query.all()
    return f'{custs}\n{trans}\n{accs}'
