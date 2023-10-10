from flask import Blueprint, jsonify, request, current_app
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.CustomError import CustomError

delete_expense_route = Blueprint('delete_expense_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@delete_expense_route.route("/api/delete/expense", methods=["DELETE"])
def delete_expense():
    try:
        expense_id = request.json["expenseId"]
        current_app.logger.info("Beginning API function delete expense with expense ID: " + str(expense_id))
        result = expense_sao.delete_expense(expense_id)
        current_app.logger.info("Finishing API function delete expense")
        return jsonify(result), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
