from flask import Blueprint

get_expenses_by_category_route = Blueprint('get_expenses_by_category_route', __name__)

@get_expenses_by_category_route.route("/api/get/expenses/category", "GET")
def get_expenses_by_category():
    pass
