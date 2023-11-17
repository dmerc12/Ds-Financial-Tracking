from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

update_category_route = Blueprint("update_category_route", __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_category_route.route("/api/update/category", methods=["PUT"])
def update_category():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update category with data: " + request_info)
        session = session_sao.get_session(request_info["sessionId"])
        updated_category = Category(category_id=request_info["categoryId"], user_id=session.user_id,
                                    category_name=request_info["categoryName"])
        result = category_sao.update_category(updated_category)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update category with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update category with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
