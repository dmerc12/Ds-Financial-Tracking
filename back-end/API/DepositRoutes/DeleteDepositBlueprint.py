from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

delete_deposit_route = Blueprint('delete_deposit_route', __name__)

deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_deposit_route.route("/api/delete/deposit", methods=["DELETE"])
def delete_deposit():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function delete deposit with deposit ID: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        result = deposit_sao.delete_deposit(request_info["depositId"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function delete deposit")
        return jsonify(result), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete deposit with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
