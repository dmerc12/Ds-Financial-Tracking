from datetime import timedelta, datetime

from flask import Blueprint, current_app, jsonify, request
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

get_all_categories_route = Blueprint('get_all_categories_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_all_categories_route.route("/api/get/all/categories", methods=["GET"])
def get_all_categories():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function get all categories")
        session = session_sao.get_session(request_info["sessionId"])
        categories = category_sao.get_all_categories(session.user_id)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        category_list = [category.convert_to_dictionary() for category in categories]
        for category in categories:
            current_app.logger.info("Finishing API function get all categories with categories with category: " +
                                    str(category.convert_to_dictionary()))
        return jsonify(category_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all categories with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
