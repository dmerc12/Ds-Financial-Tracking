from flask import Blueprint, request, current_app, jsonify

from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from Entities.CustomError import CustomError
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation

get_expenses_by_category_route = Blueprint('get_expenses_by_category_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@get_expenses_by_category_route.route("/api/get/expenses/category", methods=["PATCH"])
def get_expenses_by_category():
    try:
        category_id = int(request.json["categoryId"])
        current_app.logger.info("Beginning API function get expenses by category with category ID: " + str(category_id))
        expenses = expense_sao.get_expenses_by_category(category_id)
        expense_list = [expense.convert_to_dictionary() for expense in expenses]
        for expense in expense_list:
            current_app.logger.info("Finishing API function get expenses by category with deposits: " +
                                    str(expense))
        return jsonify(expense_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get expenses by category with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400

