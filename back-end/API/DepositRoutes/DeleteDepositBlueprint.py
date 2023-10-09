from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.CustomError import CustomError

delete_deposit_route = Blueprint('delete_deposit_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)

@delete_deposit_route.route("/api/delete/deposit", methods=["DELETE"])
def delete_deposit():
    try:
        deposit_id = request.json["depositId"]
        current_app.logger.info("Beginning API function delete deposit with deposit ID: " + str(deposit_id))
        result = deposit_sao.delete_deposit(deposit_id)
        current_app.logger.info("Finishing API function delete deposit")
        return jsonify(result), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete deposit with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
