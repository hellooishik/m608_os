from flask import Blueprint, request
from .models import Customer, Product, Order
from .schemas import CustomerSchema, ProductSchema, OrderSchema
from flask_jwt_extended import jwt_required
import math

api_bp = Blueprint("api", __name__)
from .auth import auth_bp
api_bp.register_blueprint(auth_bp, url_prefix="/auth")

def paginate(queryset, page, per_page):
    total = queryset.count()
    pages = math.ceil(total / per_page) if per_page else 1
    items = queryset.skip((page - 1) * per_page).limit(per_page)
    return items, total, pages

@api_bp.route("/customers", methods=["POST"])
@jwt_required()
def create_customer():
    data = request.get_json()
    obj = Customer(**data).save()
    return CustomerSchema().dump(obj), 201

@api_bp.route("/customers", methods=["GET"])
@jwt_required()
def list_customers():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 25))
    items, total, pages = paginate(Customer.objects, page, per_page)
    return {"data": CustomerSchema(many=True).dump(list(items)), "total": total, "pages": pages}

@api_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    if Product.objects(sku=data["sku"]).first():
        return {"message": "SKU exists"}, 400
    obj = Product(**data).save()
    return ProductSchema().dump(obj), 201

@api_bp.route("/products", methods=["GET"])
@jwt_required()
def list_products():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 25))
    items, total, pages = paginate(Product.objects, page, per_page)
    return {"data": ProductSchema(many=True).dump(list(items)), "total": total, "pages": pages}

@api_bp.route("/orders", methods=["POST"])
@jwt_required()
def create_order():
    data = request.get_json()
    customer = Customer.objects(id=data["customer"]).first()
    if not customer:
        return {"message": "invalid customer"}, 400
    obj = Order(customer=customer, total=data.get("total", 0)).save()
    return OrderSchema().dump(obj), 201

@api_bp.route("/orders", methods=["GET"])
@jwt_required()
def list_orders():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 25))
    items, total, pages = paginate(Order.objects, page, per_page)
    return {"data": OrderSchema(many=True).dump(list(items)), "total": total, "pages": pages}
