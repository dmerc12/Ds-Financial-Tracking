from datetime import timedelta, datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

get_deposits_by_category_route = Blueprint('get_deposits_by_category_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_deposits_by_category_route.route("/api/get/deposits/category", methods=["PATCH"])
def get_deposits_by_category():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function get deposits by category with category ID: " + request_info)
        session = session_sao.get_session(request_info["sessionId"])
        deposits = deposit_sao.get_deposits_by_category(request_info["categoryId"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        deposit_list = [deposit.convert_to_dictionary() for deposit in deposits]
        for deposit in deposit_list:
            current_app.logger.info("Finishing API function get deposits by category with deposits: " + str(deposit))
        return jsonify(deposit_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get deposits by category with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
