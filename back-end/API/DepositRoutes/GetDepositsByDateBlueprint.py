from flask import Blueprint

get_deposits_by_date_route = Blueprint('get_deposits_by_date_route', __name__)

@get_deposits_by_date_route.route("/api/get/deposits/date", "GET")
def get_deposits_by_date():
    pass
