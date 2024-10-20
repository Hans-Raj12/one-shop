from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oneshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    shipping_address = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __repr__(self):
        return f'{self.name} - {self.email}'

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    order_details = db.relationship('OrderDetails', backref='product', lazy=True)

    def __repr__(self):
        return f'{self.name} - {self.price}'

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    order_details = db.relationship('OrderDetails', backref='order', lazy=True)

    def __repr__(self):
        return f'{self.id} - {self.order_date} - {self.status}'

# Define the OrderDetails model
class OrderDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.id} - {self.quantity} - {self.price}'


# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    return render_template('HomePage.html')

@app.route('/cart')
def cart():
    return render_template('/cart.html')

@app.route('/items')
def items():
    return render_template('/items.html')

@app.route('/kids')
def kids():
    return render_template('/kids.html')

@app.route('/mens')
def mens():
    return render_template('/mens.html')

@app.route('/womens')
def womens():
    return render_template('womens.html')

if __name__ == '__main__':
    app.run(debug=True)