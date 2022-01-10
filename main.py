from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


deals = db.Table('deals',
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
    db.Column('pc_id', db.Integer, db.ForeignKey('pc.id'), primary_key=True)
    )


class CustomerModel(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    pcs = db.relationship('CustomerModel', secondary=deals, backref='customers')

    def __repr__(self):
        return f"Customer(name={self.name}, surname={self.surname}, email={self.email})"


class PCModel(db.Model):
    __tablename__ = 'pc'
    id = db.Column(db.String, primary_key=True)
    cpu = db.Column(db.Integer, nullable=False)
    ram = db.Column(db.Integer, nullable=False)
    ssd = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"PC(id={id}, cpu={self.cpu}, ram={self.ram}, ssd={self.ssd}, price={self.price})"


db.create_all()

customer_post_args = reqparse.RequestParser()
customer_post_args.add_argument('name', type=str, help='Name of the customer is required', required=True)
customer_post_args.add_argument('surname', type=str, help='Surname of the customer is required', required=True)
customer_post_args.add_argument('email', type=str, help='Email of the customer is required', required=True)


pc_post_args = reqparse.RequestParser()
pc_post_args.add_argument('cpu', type=str, help='CPU of the PC is required', required=True)
pc_post_args.add_argument('ram', type=int, help='RAM of the PC is required', required=True)
pc_post_args.add_argument('ssd', type=int, help='SSD of the PC is required', required=True)
pc_post_args.add_argument('price', type=int, help='Price of the PC is required', required=True)


customer_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'surname': fields.String,
    'email': fields.String
}

pc_resource_fields = {
    'id': fields.Integer,
    'cpu': fields.String,
    'ram': fields.Integer,
    'ssd': fields.Integer,
    'price': fields.Integer
}

deal_resource_fields = {
    'customer_id': fields.Integer,
    'pc_id': fields.Integer
}


class Customer(Resource):
    @marshal_with(customer_resource_fields)
    def get(self, customer_id):
        result = CustomerModel.query.filter_by(id=customer_id).first()
        if not result:
            abort(404, message='Could not find the customer with this id')
        return result

    @marshal_with(customer_resource_fields)
    def post(self, customer_id):
        args = customer_post_args.parse_args()
        result = CustomerModel.query.filter_by(id=customer_id).first()
        if result:
            abort(409, message='Customer already exists')
        customer = CustomerModel(id=customer_id, name=args['name'], surname=args['surname'], email=args['email'])
        db.session.add(customer)
        db.session.commit()

        return customer, 201

    @marshal_with(customer_resource_fields)
    def delete(self, customer_id):
        result = CustomerModel.query.filter_by(id=customer_id).first()
        if not result:
            abort(404, message='Could not find the customer with this id, cannot delete')
        db.session.delete(result)
        db.session.commit()

        return {"message": "Customer deleted successfully"}, 204


class PC(Resource):
    @marshal_with(pc_resource_fields)
    def get(self, pc_id):
        result = PCModel.query.filter_by(id=pc_id).first()
        if not result:
            abort(404, message='Could not find the PC with this id')
        return result

    @marshal_with(pc_resource_fields)
    def post(self, pc_id):
        args = pc_post_args.parse_args()
        result = PCModel.query.filter_by(id=pc_id).first()
        if result:
            abort(409, message='PC already exists')
        pc = PCModel(id=pc_id, cpu=args['cpu'], ram=args['ram'], ssd=args['ssd'], price=args['price'])
        db.session.add(pc)
        db.session.commit()

        return pc, 201

    @marshal_with(pc_resource_fields)
    def delete(self, pc_id):
        result = PCModel.query.filter_by(id=pc_id).first()
        if not result:
            abort(404, message='Could not find the PC with this id, cannot delete')
        db.session.delete(result)
        db.session.commit()

        return {"message": "PC deleted successfully"}, 204




api.add_resource(Customer, "/customer/<int:customer_id>")
api.add_resource(PC, "/pc/<int:pc_id>")


if __name__ == "__main__":
    app.run(debug=True)