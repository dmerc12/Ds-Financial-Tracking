from flask import Blueprint, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.CustomError import CustomError

get_all_expenses_route = Blueprint('get_all_expenses_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@get_all_expenses_route.route("/api/get/all/expenses", methods=["GET"])
def get_all_expenses():
    try:
        current_app.logger.info("Beginning API function get all expenses")
        expenses = expense_sao.get_all_expenses()
        expense_list = [expense.convert_to_dictionary() for expense in expenses]
        for expense in expense_list:
            current_app.logger.info("Finishing API function get all expenses with expenses: " + str(expense))
        return jsonify(expense_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all expenses with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
