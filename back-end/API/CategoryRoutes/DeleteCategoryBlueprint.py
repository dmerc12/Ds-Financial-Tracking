from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.CustomError import CustomError
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation

delete_category_route = Blueprint("delete_category_route", __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_category_route.route("/api/delete/category", methods=["DELETE"])
def delete_category():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function delete category with category ID: " + request_info)
        session = session_sao.get_session(request_info["sessionId"])
        result = category_sao.delete_category(request_info["categoryId"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function delete category")
        return jsonify(result), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete category with error: " + str(error))
        response = {"message": str(error)}
        return jsonify(response), 400
