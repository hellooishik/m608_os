from mongoengine import Document, StringField, FloatField, IntField, ReferenceField, DateTimeField
from datetime import datetime

class User(Document):
    username = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    role = StringField(default="user")

class Customer(Document):
    name = StringField(required=True)
    email = StringField(unique=True)
    phone = StringField()
    created_at = DateTimeField(default=datetime.utcnow)

class Product(Document):
    name = StringField(required=True)
    sku = StringField(required=True, unique=True)
    price = FloatField(required=True)
    stock = IntField(default=0)

class Order(Document):
    customer = ReferenceField(Customer, required=True)
    total = FloatField(default=0.0)
    status = StringField(default="pending")
    created_at = DateTimeField(default=datetime.utcnow)
