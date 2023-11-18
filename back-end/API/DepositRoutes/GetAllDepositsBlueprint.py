from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.DepositDAL.DepositDALImplementation import DepositDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.DepositSAL.DepositSALImplementation import DepositSALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

get_all_deposits_route = Blueprint('get_all_deposits_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
deposit_dao = DepositDALImplementation()
deposit_sao = DepositSALImplementation(deposit_dao, category_sao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_all_deposits_route.route("/api/get/all/deposits", methods=["GET"])
def get_all_deposits():
    try:
        session_id = request.json["sessionId"]
        current_app.logger.info("Beginning API function get all deposits with info: " + str(session_id))
        session = session_sao.get_session(session_id)
        deposits = deposit_sao.get_all_deposits(session.user_id)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        deposit_list = [deposit.convert_to_dictionary() for deposit in deposits]
        for deposit in deposit_list:
            current_app.logger.info("Finishing API function get all deposits with deposits: " + str(deposit))
        return jsonify(deposit_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all deposits with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
