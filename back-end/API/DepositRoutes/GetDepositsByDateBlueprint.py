from datetime import timedelta, datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

get_deposits_by_date_route = Blueprint('get_deposits_by_date_route', __name__)

deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_deposits_by_date_route.route("/api/get/deposits/date", methods=["PATCH"])
def get_deposits_by_date():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function get deposits by date with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        date = datetime.strptime(request_info["date"], "%Y-%m-%d").date()
        deposits = deposit_sao.get_deposits_by_date(date)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        deposit_list = [deposit.convert_to_dictionary() for deposit in deposits]
        for deposit in deposit_list:
            current_app.logger.info("Finishing API function get deposits by date with deposits: " + str(deposit))
        return jsonify(deposit_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get deposits by date with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
