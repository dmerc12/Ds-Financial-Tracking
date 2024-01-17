from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

delete_expense_route = Blueprint('delete_expense_route', __name__)

expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@delete_expense_route.route("/api/delete/expense", methods=["DELETE"])
def delete_expense():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function delete expense with info: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        result = expense_sao.delete_expense(request_info["expenseId"])
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function delete expense")
        return jsonify(result), 202
    except CustomError as error:
        current_app.logger.error("Error with API function delete expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
