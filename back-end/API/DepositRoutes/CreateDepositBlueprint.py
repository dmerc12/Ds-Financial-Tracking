from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

create_deposit_route = Blueprint('create_deposit_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)

@create_deposit_route.route("/api/create/deposit", methods=["POST"])
def create_deposit():
    try:
        deposit_info = request.json
        current_app.logger.info("Beginning API function create deposit with data: " + str(deposit_info))
        new_deposit = Deposit(deposit_id=0, category_id=deposit_info["categoryId"], date=deposit_info["date"],
                              description=deposit_info["description"], amount=float(deposit_info["amount"]))
        result = deposit_sao.create_deposit(new_deposit)
        current_app.logger.info("Finishing API function create deposit with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create deposit with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
