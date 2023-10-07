from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.Category import Category
from Entities.CustomError import CustomError

create_category_route = Blueprint('create_category_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

@create_category_route.route("/api/create/category", methods=["POST"])
def create_category():
    try:
        category_info = request.json
        current_app.logger.info("Beginning API function create category with data: " + str(category_info))
        new_category = Category(category_id=0, category_name=category_info["categoryName"])
        result = category_sao.create_category(new_category)
        current_app.logger.info("Finishing API function create category with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create category with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
