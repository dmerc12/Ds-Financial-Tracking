from datetime import timedelta, datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError
from Entities.Deposit import Deposit

create_deposit_route = Blueprint('create_deposit_route', __name__)

deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@create_deposit_route.route("/api/create/deposit", methods=["POST"])
def create_deposit():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function create deposit with data: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        new_deposit = Deposit(deposit_id=0, user_id=session.user_id, category_id=request_info["categoryId"],
                              deposit_date=request_info["date"], description=request_info["description"],
                              amount=float(request_info["amount"]))
        result = deposit_sao.create_deposit(new_deposit)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function create deposit with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create deposit with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
