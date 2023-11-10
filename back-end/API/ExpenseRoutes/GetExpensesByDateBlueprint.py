from datetime import datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.CategoryDAL.CategoryDALImplementation import CategoryDALImplementation
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.CategorySAL.CategorySALImplementation import CategorySALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from Entities.CustomError import CustomError

get_expenses_by_date_route = Blueprint('get_expenses_by_date_route', __name__)

category_dao = CategoryDALImplementation()
category_sao = CategorySALImplementation(category_dao)
expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao, category_sao)

@get_expenses_by_date_route.route("/api/get/expenses/date", methods=["PATCH"])
def get_expenses_by_date():
    try:
        date = datetime.strptime(request.json["date"], "%Y-%m-%d").date()
        current_app.logger.info("Beginning API function get expenses by date with date: " + str(date))
        expenses = expense_sao.get_expenses_by_date(date)
        expense_list = [expense.convert_to_dictionary() for expense in expenses]
        for expense in expense_list:
            current_app.logger.info("Finishing API function get expenses by date with expenses: " +
                                    str(expense))
        return jsonify(expense_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get expenses by date with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
