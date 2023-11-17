from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from Entities.User import User
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation

update_user_route = Blueprint("update_user_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_user_route.route("/api/update/user", methods=["PUT"])
def update_user():
    try:
        updated_info = request.json
        current_app.logger.info("Beginning API function update user with updated info: " + updated_info)
        session = session_sao.get_session(updated_info["sessionId"])
        user = User(user_id=session.user_id, first_name=updated_info["firstName"], last_name=updated_info["lastName"],
                    email=updated_info["email"], password="")
        updated_user = user_sao.update_user(user)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update user with user: " +
                                str(updated_user.convert_to_dictionary()))
        return jsonify(updated_user), 200
    except CustomError as error:
        current_app.logger.error("Error with API function update user with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
