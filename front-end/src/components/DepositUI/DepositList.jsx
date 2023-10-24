import { CreateDepositModal } from "./CreateDepositModal";
import { UpdateDepositModal } from "./UpdateDepositModal";
import { DeleteDepositModal } from "./DeleteDepositModal";
import { useFetch } from "../../hooks/useFetch";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { toast } from "react-toastify";

export const DepositList = () => {
    const [deposits, setDeposits] = useState([]);
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(false);
    const [failedToFetchCategories, setFailedToFetchCategories] = useState(false);
    const [failedToFetchDeposits, setFailedToFetchDeposits] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const goBack = () => {
        navigate('/home');
        setFailedToFetchCategories(false);
        setFailedToFetchDeposits(false);
    };

    let depositRows = [];

    const fetchCategories = async () => {
        setLoading(true);
        setFailedToFetchCategories(false);
        setFailedToFetchSubmission(false);
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
                toast.warn(error.message, {toastId: 'customId'});
             }
        }
    };

    const fetchDeposits = async () => {
        setLoading(true);
        setFailedToFetchDeposits(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/deposits', 'GET');

            if (responseStatus === 200) {
                setDeposits(data);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetchDeposits(true)
            } else {
                setLoading(false);
                toast.warn(error.message, {toastId: 'customId'});
            }
        }
    }

    useEffect(() => {
        fetchDeposits();
        fetchCategories();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    if (deposits.length > 0) {
        for (let i=0; i < deposits.length; i++) {
            const deposit = deposits[i];
            depositRows.push(
                <tr key={deposit.depositId}>
                    <td className="table-data">{deposit.depositId}</td>
                    <td className="table-data">{deposit.categoryId}</td>
                    <td className="table-data">{deposit.date}</td>
                    <td className="table-data">{deposit.description}</td>
                    <td className="table-data">{deposit.amount}</td>
                    <td className="table-data">
                        <UpdateDepositModal deposit={deposit} categories={categories} fetchDeposits={fetchDeposits} />
                        <DeleteDepositModal deposit={deposit} fetchDeposits={fetchDeposits} />
                    </td>
                </tr>
            )
        }
    }

    return (
        <>
            <CreateDepositModal categories={categories} fetchDeposits={fetchDeposits} />
            {loading ? (
                <div className="loading-indicator">
                    <FaSpinner className="spinner" />
                </div>  
            ) : failedToFetchDeposits ? (
                <div className='failed-to-fetch'>
                    <AiOutlineExclamationCircle className='warning-icon'/>
                    <p>Cannot connect to the back end server.</p>
                    <p>Please check your internet connection and try again.</p>
                    <button className='retry-button' onClick={fetchDeposits}>
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
            ) : deposits.length === 0 ? (
                <div className="empty-list">No deposits have been created yet. Click the Add Deposit button to create a new deposit.</div>
            ) : (
                <div className="list">
                    <table className="table">
                        <thead>
                            <tr>
                                <th className="table-head">Deposit ID</th>
                                <th className="table-head">Category ID</th>
                                <th className="table-head">Date</th>
                                <th className="table-head">Description</th>
                                <th className="table-head">Amount</th>
                            </tr>
                        </thead>
                        <tbody>
                            {depositRows}
                        </tbody>
                    </table>
                </div>
            )}
        </>
    );
}