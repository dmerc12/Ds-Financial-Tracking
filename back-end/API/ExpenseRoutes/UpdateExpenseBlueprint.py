from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError
from Entities.Expense import Expense

update_expense_route = Blueprint('update_expense_route', __name__)

expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@update_expense_route.route("/api/update/expense", methods=["PUT"])
def update_expense():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function update expense with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        updated_expense = Expense(expense_id=request_info["expenseId"], user_id=session.user_id,
                                  category_id=request_info["categoryId"], expense_date=request_info["date"],
                                  description=request_info["description"], amount=request_info["amount"])
        result = expense_sao.update_expense(updated_expense)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function update expense with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 202
    except CustomError as error:
        current_app.logger.error("Error with API function update expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
