from datetime import timedelta, datetime

from flask import Blueprint, jsonify, request, current_app
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError

get_all_expenses_route = Blueprint('get_all_expenses_route', __name__)

expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@get_all_expenses_route.route("/api/get/all/expenses", methods=["GET"])
def get_all_expenses():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function get all expenses")
        session = session_sao.get_session(request_info["sessionId"])
        expenses = expense_sao.get_all_expenses(session.user_id)
        expense_list = [expense.convert_to_dictionary() for expense in expenses]
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        for expense in expense_list:
            current_app.logger.info("Finishing API function get all expenses with expenses: " + str(expense))
        return jsonify(expense_list), 200
    except CustomError as error:
        current_app.logger.error("Error with API function get all expenses with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
