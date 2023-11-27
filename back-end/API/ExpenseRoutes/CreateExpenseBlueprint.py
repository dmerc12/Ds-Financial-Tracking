from datetime import timedelta, datetime

from flask import Blueprint, request, current_app, jsonify
from DAL.ExpenseDAL.ExpenseDALImplementation import ExpenseDALImplementation
from SAL.ExpenseSAL.ExpenseSALImplementation import ExpenseSALImplementation
from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from SAL.SessionSAL.SessionSALImplementation import SessionSALImplementation
from Entities.CustomError import CustomError
from Entities.Expense import Expense

create_expense_route = Blueprint('create_expense_route', __name__)

expense_dao = ExpenseDALImplementation()
expense_sao = ExpenseSALImplementation(expense_dao)
session_dao = SessionDALImplementation()
session_sao = SessionSALImplementation(session_dao)

@create_expense_route.route("/api/create/expense", methods=["POST"])
def create_expense():
    try:
        request_info = request.json
        current_app.logger.info("Beginning API function create expense with data: " + str(request_info))
        session = session_sao.get_session(request_info["sessionId"])
        new_expense = Expense(expense_id=0, user_id=session.user_id, category_id=request_info["categoryId"],
                              expense_date=request_info["date"], description=request_info["description"],
                              amount=request_info["amount"])
        result = expense_sao.create_expense(new_expense)
        session.expiration = datetime.now() + timedelta(minutes=15)
        session_sao.update_session(session)
        current_app.logger.info("Finishing API function create expense with result: " +
                                str(result.convert_to_dictionary()))
        return jsonify(result.convert_to_dictionary()), 201
    except CustomError as error:
        current_app.logger.error("Error with API function create expense with error: " + str(error))
        response = {
            "message": str(error)
        }
        return jsonify(response), 400
