from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from Entities.CustomError import CustomError
from Entities.User import User

change_email_route = Blueprint("change_email_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@change_email_route.route("/api/update/user", methods=["PUT"])
def update_user():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update user with updated info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        user = User(user_id=session.user_id, email=request_info["email"], password="")
        result = user_sao.change_email(user)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update user with result: " + str(result))
        return jsonify(result), 200
    except CustomError as error:
        current_app.logger.error("Error with API function update user with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
