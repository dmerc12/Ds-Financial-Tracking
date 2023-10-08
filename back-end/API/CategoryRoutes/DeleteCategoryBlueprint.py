from flask import Blueprint, jsonify, request, current_app

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.CustomError import CustomError

delete_category_route = Blueprint("delete_category_route", __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

@delete_category_route.route("/api/delete/category", methods=["DELETE"])
def delete_category():
    try:
        category_id = request.json["categoryId"]
        current_app.logger.info("Beginning API function delete category with category ID: " + str(category_id))
        result = category_sao.delete_category(category_id)
        current_app.logger.info("Finishing API function delete category")
        return jsonify({"message": str(result)}), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete category with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
