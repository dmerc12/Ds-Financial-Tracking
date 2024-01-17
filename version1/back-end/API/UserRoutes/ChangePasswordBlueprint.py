from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.User import User

change_password_route = Blueprint("change_password_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@change_password_route.route("/api/change/password", methods=["PUT"])
def change_password():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function change password with password form info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        user = user_sao.get_user_by_id(session.user_id)
        user = User(user.user_id, user.email, request_info["password"])
        result = user_sao.change_password(user, request_info["confirmationPassword"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function change password with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function change password with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
