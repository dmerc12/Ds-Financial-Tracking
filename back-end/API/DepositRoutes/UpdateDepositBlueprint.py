from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.Deposit import Deposit
from Entities.CustomError import CustomError

update_deposit_route = Blueprint('update_deposit_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_deposit_route.route("/api/update/deposit", methods=["PUT"])
def update_deposit():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update deposit with data: " + request_info)
        session = session_sao.get_session(request_info["sessionId"])
        updated_deposit = Deposit(deposit_id=request_info["depositId"], user_id=session.user_id,
                                  category_id=request_info["categoryId"], deposit_date=request_info["date"],
                                  description=request_info["description"], amount=request_info["amount"])
        result = deposit_sao.update_deposit(updated_deposit)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update deposit with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update deposit with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
