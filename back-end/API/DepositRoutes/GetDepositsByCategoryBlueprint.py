from flask import Blueprint

get_deposits_by_category_route = Blueprint('get_deposits_by_category_route', __name__)

@get_deposits_by_category_route.route("/api/get/deposits/category", "GET")
def get_deposits_by_category():
    pass
