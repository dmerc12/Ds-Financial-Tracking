from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

update_deposit_route = Blueprint('update_deposit_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)

@update_deposit_route.route("/api/update/deposit", methods=["PUT"])
def update_deposit():
    try:
        updated_info = request.json
        current_app.logger.info("Beginning API function update deposit with data: " + str(updated_info))
        updated_deposit = Deposit(deposit_id=updated_info["depositId"], category_id=updated_info["categoryId"],
                                  deposit_date=updated_info["date"], description=updated_info["description"],
                                  amount=updated_info["amount"])
        result = deposit_sao.update_deposit(updated_deposit)
        current_app.logger.info("Finishing API function update deposit with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update deposit with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
