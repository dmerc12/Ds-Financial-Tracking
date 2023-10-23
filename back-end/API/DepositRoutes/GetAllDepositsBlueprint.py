from flask import Blueprint, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.CustomError import CustomError

get_all_deposits_route = Blueprint('get_all_deposits_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)

@get_all_deposits_route.route("/api/get/all/deposits", methods=["GET"])
def get_all_deposits():
    try:
        current_app.logger.info("Beginning API function get all deposits")
        deposits = deposit_sao.get_all_deposits()
        deposit_list = [deposit.convert_to_dictionary() for deposit in deposits]
        for deposit in deposit_list:
            current_app.logger.info("Finishing API function get all deposits with deposits: " +
                                    str(deposit))
        return jsonify(deposit_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all deposits with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
