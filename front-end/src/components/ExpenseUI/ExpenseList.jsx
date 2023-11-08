import PropTypes from 'prop-types';

import { CreateExpenseModal } from "./CreateExpenseModal";
import { UpdateExpenseModal } from "./UpdateExpenseModal";
import { DeleteExpenseModal } from "./DeleteExpenseModal";
import { useFetch } from "../../hooks/useFetch";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";

export const ExpenseList = ({ toastRef }) => {
    const [expenses, setExpenses] = useState([]);
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(false);
    const [failedToFetchCategories, setFailedToFetchCategories] = useState(false);
    const [failedToFetchExpenses, setFailedToFetchExpenses] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const goBack = () => {
        navigate('/home');
        setFailedToFetchCategories(false);
        setFailedToFetchExpenses(false);
    };

    let expenseRows = [];

    const fetchCategories = async () => {
        setLoading(true);
        setFailedToFetchCategories(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/categories', 'GET');

            if (responseStatus === 200) {
                setCategories(data);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetchCategories(true);
             } else {
                setLoading(false);
                toastRef.current.addToast({ mode: 'error', message: error.message});
             }
        }
    };

    const fetchExpenses = async () => {
        setLoading(true);
        setFailedToFetchExpenses(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/expenses', 'GET');

            if (responseStatus === 200) {
                setExpenses(data);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetchExpenses(true)
            } else {
                setLoading(false);
                toastRef.current.addToast({ mode: 'error', message: error.message});
            }
        }
    }

    useEffect(() => {
        fetchExpenses();
        fetchCategories();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    if (expenses.length > 0) {
        for (let i=0; i < expenses.length; i++) {
            const expense = expenses[i];
            expenseRows.push(
                <tr key={expense.expenseId}>
                    <td className="table-data">{expense.expenseId}</td>
                    <td className="table-data">{expense.categoryId}</td>
                    <td className="table-data">{expense.date}</td>
                    <td className="table-data">{expense.description}</td>
                    <td className="table-data">{expense.amount}</td>
                    <td className="table-data">
                        <UpdateExpenseModal toastRef={toastRef} expense={expense} categories={categories} fetchExpenses={fetchExpenses} />
                        <DeleteExpenseModal toastRef={toastRef} expense={expense} fetchExpenses={fetchExpenses} />
                    </td>
                </tr>
            )
        }
    }

    return (
        <>
            <CreateExpenseModal toastRef={toastRef} categories={categories} fetchExpenses={fetchExpenses} />
            {loading ? (
                <div className="loading-indicator">
                    <FaSpinner className="spinner" />
                </div>  
            ) : failedToFetchExpenses ? (
                <div className='failed-to-fetch'>
                    <AiOutlineExclamationCircle className='warning-icon'/>
                    <p>Cannot connect to the back end server.</p>
                    <p>Please check your internet connection and try again.</p>
                    <button className='retry-button' onClick={fetchExpenses}>
                        <FaSync className='retry-icon'/> Retry
                    </button>
                    <button className='back-button' onClick={goBack}>Go Back</button>
                </div>
            ) : failedToFetchCategories ? (
                <div className='failed-to-fetch'>
                  <AiOutlineExclamationCircle className='warning-icon' />
                  <p>Cannot connect to the back end server.</p>
                  <p>Please check your internet connection and try again.</p>
                  <button className='retry-button' onClick={fetchCategories}>
                     <FaSync className='retry-icon' />
                  </button>
                  <button className='back-button' onClick={goBack}>Go Back</button>
               </div>
            ) : expenses.length === 0 ? (
                <div className="empty-list">No expenses have been created yet. Click the Add Expense button to create a new expense.</div>
            ) : (
                <div className="list">
                    <table className="table">
                        <thead>
                            <tr>
                                <th className="table-head">Expense ID</th>
                                <th className="table-head">Category ID</th>
                                <th className="table-head">Date</th>
                                <th className="table-head">Description</th>
                                <th className="table-head">Amount</th>
                            </tr>
                        </thead>
                        <tbody>
                            {expenseRows}
                        </tbody>
                    </table>
                </div>
            )}
        </>
    );
};

ExpenseList.propTypes = {
    toastRef: PropTypes.object.isRequired
};
