from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.Expense import Expense
from Entities.CustomError import CustomError

create_expense_route = Blueprint('create_expense_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@create_expense_route.route("/api/create/expense", methods=["POST"])
def create_expense():
    try:
        expense_info = request.json
        current_app.logger.info("Beginning API function create expense with data: " + str(expense_info))
        new_expense = Expense(expense_id=0, category_id=expense_info["categoryId"], date=expense_info["date"],
                              description=expense_info["description"], amount=expense_info["amount"])
        result = expense_sao.create_expense(new_expense)
        current_app.logger.info("Finishing API function create expense with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
