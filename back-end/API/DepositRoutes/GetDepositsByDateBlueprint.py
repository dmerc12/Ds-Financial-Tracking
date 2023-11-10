from datetime import datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.CustomError import CustomError

get_deposits_by_date_route = Blueprint('get_deposits_by_date_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)

@get_deposits_by_date_route.route("/api/get/deposits/date", methods=["PATCH"])
def get_deposits_by_date():
    try:
        deposits_date = datetime.strptime(request.json["date"], "%Y-%m-%d").date()
        current_app.logger.info("Beginning API function get deposits by date with category ID: " + str(deposits_date))
        deposits = deposit_sao.get_deposits_by_date(deposits_date)
        deposit_list = [deposit.convert_to_dictionary() for deposit in deposits]
        for deposit in deposit_list:
            current_app.logger.info("Finishing API function get deposits by date with deposits: " +
                                    str(deposit))
        return jsonify(deposit_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get deposits by date with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
