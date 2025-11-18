from marshmallow import Schema, fields

class RegisterSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class CustomerSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email()
    phone = fields.Str()

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    sku = fields.Str(required=True)
    price = fields.Float(required=True)
    stock = fields.Int()

class OrderSchema(Schema):
    id = fields.Str(dump_only=True)
    customer = fields.Str(required=True)
    total = fields.Float()
    status = fields.Str()
