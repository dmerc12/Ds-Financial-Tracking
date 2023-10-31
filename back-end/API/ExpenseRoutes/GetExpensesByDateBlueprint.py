from flask import Blueprint

get_expenses_by_date_route = Blueprint('get_expenses_bydate_route', __name__)

@get_expenses_by_date_route.route("/api/get/expenses/date", "GET")
def get_expenses_by_date():
    pass
