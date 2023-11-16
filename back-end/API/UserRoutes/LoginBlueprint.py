import datetime

from flask import Blueprint, current_app, jsonify, request

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from Entities.Session import Session
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation

login_route = Blueprint("login_route", __name__)

user_dao = UserDALImplementation()
user_sao = UserSALImplementation(user_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@login_route.route("/api/login", methods=["POST"])
def login():
    try:
        login_form = request.json
        current_app.logger.info("Beginning API function login with login info: " + login_form)
        user = user_sao.login(email=login_form["email"], password=login_form["password"])
        session_info = Session(0, user.user_id, datetime.datetime.now() + datetime.timedelta(minutes=15))
        new_session = session_sao.create_session(session_info)
        current_app.logger.info("Finishing API function login with session: " +
                                str(new_session.convert_to_dictionary()))
        response = {"sessionId": new_session.session_id}
        return jsonify(response), 200
    except CustomError as error:
        current_app.logger.error("Error with API function login with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
