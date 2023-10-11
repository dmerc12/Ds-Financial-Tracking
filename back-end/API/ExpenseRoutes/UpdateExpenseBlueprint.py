from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.Expense import Expense
from Entities.CustomError import CustomError

update_expense_route = Blueprint('update_expense_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@update_expense_route.route("/api/update/expense", methods=["PUT"])
def update_expense():
    try:
        updated_info = request.json
        current_app.logger.info("Beginning API function update expense with data: " + str(updated_info))
        updated_expense = Expense(expense_id=updated_info["expenseId"], category_id=updated_info["categoryId"],
                                  date=updated_info["date"], description=updated_info["description"],
                                  amount=updated_info["amount"])
        result = expense_sao.update_expense(updated_expense)
        current_app.logger.info("Finishing API function update expense with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
