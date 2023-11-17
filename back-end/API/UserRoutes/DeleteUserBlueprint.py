from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation

delete_user_route = Blueprint("delete_user_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_user_route.route("/api/delete/user", methods=["DELETE"])
def delete_user():
    try:
        delete_info = request.json
        current_app.logger.info("Beginning API function delete user with info: " + str(delete_info))
        session = session_sao.get_session(delete_info["sessionId"])
        session_sao.delete_all_sessions(session.user_id)
        # delete all deposits
        # delete all expenses
        # delete all categories
        result = user_sao.delete_user(session.user_id)
        current_app.logger.info("Finishing API function delete user with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with DAL function delete user with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
