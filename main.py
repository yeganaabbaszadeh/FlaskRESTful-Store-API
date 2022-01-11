from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
import sqlite3


app = Flask(__name__)
api = Api(app)
conn = sqlite3.connect('database.db', check_same_thread=False)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    email TEXT
)""")

c.execute("""CREATE TABLE IF NOT EXISTS pc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpu TEXT,
    ram TEXT,
    ssd TEXT,
    price INTEGER
)""")

c.execute("""CREATE TABLE IF NOT EXISTS deal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER REFERENCES customer (id),
    pc_id INTEGER REFERENCES pc (id)
)""")


customer_parser = reqparse.RequestParser()
customer_parser.add_argument('name', type=str)
customer_parser.add_argument('surname', type=str)
customer_parser.add_argument('email', type=str)


pc_parser = reqparse.RequestParser()
pc_parser.add_argument('cpu', type=str)
pc_parser.add_argument('ram', type=str)
pc_parser.add_argument('ssd', type=str)
pc_parser.add_argument('price', type=int)


deal_parser = reqparse.RequestParser()
deal_parser.add_argument('customer_id', type=int)
deal_parser.add_argument('pc_id', type=int)


class AddCustomer(Resource):
    def post(self):
        args = customer_parser.parse_args()
        name = args['name']
        surname = args['surname']
        email = args['email']
        c.execute("INSERT INTO customer (name, surname, email) VALUES(?, ?, ?)", (name, surname, email))
        conn.commit()
        return {"message": "Customer created"}, 201


class Customer(Resource):
    def get(self, customer_id):
        c.execute("SELECT * FROM customer WHERE id = ?", (customer_id, ))
        result = c.fetchall()
        if not result:
            abort(404, message='Could not find the customer with this id')
        return jsonify(result)

    
    def delete(self, customer_id):
        c.execute("SELECT 1 FROM customer WHERE id = ?", (customer_id, ))
        result = c.fetchone()
        if not result:
            abort(404, message='Could not find the customer with this id, cannot delete')
        c.execute("DELETE FROM customer WHERE id = ?", (customer_id, ))
        conn.commit()
        return {"message": "Customer deleted"}


class AddPC(Resource):
    def post(self):
        args = pc_parser.parse_args()
        cpu = args['cpu']
        ram = args['ram']
        ssd = args['ssd']
        price = args['price']
        c.execute("INSERT INTO pc (cpu, ram, ssd, price) VALUES(?, ?, ?, ?)", (cpu, ram, ssd, price))
        conn.commit()
        return {"message": "PC created"}, 201


class PC(Resource):
    def get(self, pc_id):
        c.execute("SELECT * FROM pc WHERE id = ?", (pc_id, ))
        result = c.fetchall()
        if not result:
            abort(404, message='Could not find the PC with this id')
        return jsonify(result)

    def delete(self, pc_id):
        c.execute("SELECT 1 FROM pc WHERE id = ?", (pc_id, ))
        result = c.fetchone()
        if not result:
            abort(404, message='Could not find the PC with this id, cannot delete')
        c.execute("DELETE FROM pc WHERE id = ?", (pc_id, ))
        conn.commit()
        return {"message": "PC deleted"}


class AddDeal(Resource):
    def post(self):
        args = deal_parser.parse_args()
        customer_id = args['customer_id']
        pc_id = args['pc_id']
        c.execute("INSERT INTO deal (customer_id, pc_id) VALUES (?, ?)", (customer_id, pc_id))
        conn.commit()
        return {"message": "Deal added"}, 201


class ShowDealsByCustomer(Resource):
    def get(self, customer_id):
        c.execute("SELECT customer_id, pc_id FROM deal WHERE customer_id = ?", (customer_id, ))
        result = c.fetchall()
        if not result:
            abort(404, message='No deals')
        return jsonify(result)


class ShowDealsByPC(Resource):
    def get(self, pc_id):
        c.execute("SELECT customer_id FROM deal WHERE pc_id = ?", (pc_id, ))
        result = c.fetchall()
        if not result:
            abort(404, message='No deals')
        return jsonify(result)


class BestBuyer(Resource):
    def get(self):
        c.execute("""SELECT customer.name, SUM(pc.price) AS 'Price'
        FROM customer, pc, deal
        WHERE customer.id = deal.customer_id
        AND pc.id = deal.pc_id
        GROUP BY customer.id
        ORDER BY 'Price' ASC""")
        result = c.fetchall()
        if not result:
            abort(404, message='No best buyer')
        return jsonify(result[0])


api.add_resource(AddCustomer, "/customer")
api.add_resource(Customer, "/customers/<int:customer_id>")
api.add_resource(AddPC, "/pc")
api.add_resource(PC, "/pcs/<int:pc_id>")
api.add_resource(AddDeal, "/deal")
api.add_resource(ShowDealsByCustomer, "/deals/showdeals/<int:customer_id>")
api.add_resource(ShowDealsByPC, "/deals/showcustomers/<int:pc_id>")
api.add_resource(BestBuyer, "/bestbuyer")


if __name__ == "__main__":
    app.run(debug=True)
