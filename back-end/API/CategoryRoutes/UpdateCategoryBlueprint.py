from flask import Blueprint, jsonify, request, current_app

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

update_category_route = Blueprint("update_category_route", __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

@update_category_route.route("/api/update/category", methods=["PUT"])
def update_category():
    try:
        updated_info = request.json
        current_app.logger.info("Beginning API function update category with data: " + str(updated_info))
        updated_category = Category(category_id=updated_info["categoryId"], category_name=updated_info["categoryName"])
        result = category_sao.update_category(updated_category)
        current_app.logger.info("Finishing API function update category with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update category with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
