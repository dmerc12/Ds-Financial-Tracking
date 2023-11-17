from datetime import timedelta, datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

create_category_route = Blueprint('create_category_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@create_category_route.route("/api/create/category", methods=["POST"])
def create_category():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function create category with name: " + request_info)
        session = session_sao.get_session(request_info)
        new_category = Category(category_id=0, user_id=session.user_id, category_name=request_info["categoryName"])
        result = category_sao.create_category(new_category)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function create category with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create category with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
