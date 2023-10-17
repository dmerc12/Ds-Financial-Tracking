from flask import Blueprint, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from Entities.CustomError import CustomError

get_all_categories_route = Blueprint('get_all_categories_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)

@get_all_categories_route.route("/api/get/all/categories", methods=["GET"])
def get_all_categories():
    try:
        current_app.logger.info("Beginning API function get all categories")
        categories = category_sao.get_all_categories()
        category_list = [category.convert_to_dictionary() for category in categories]
        current_app.logger.info("Finishing API function get all categories with categories")
        return jsonify(category_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all categories with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
