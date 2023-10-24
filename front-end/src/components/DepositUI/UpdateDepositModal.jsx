import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FiEdit } from 'react-icons/fi';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const UpdateDepositModal = ({ deposit, categories, fetchDeposits }) => {
    const [depositForm, setDepositForm] = useState({
        depositId: deposit.depositId,
        categoryId: deposit.categoryId,
        date: deposit.date,
        description: deposit.description,
        amount: deposit.amount
    });
    const [visible, setVisible] = useState(false);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const { fetchData } = useFetch();

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        setFailedToFetch(false);
    };

    const onChange = (event) => {
        const { name, value } = event.target;
        if (name === 'categoryId' | name === 'amount') {
            setDepositForm((prevForm) => ({
                ...prevForm,
                [name]: Number(value)
            }));
        } else {
            setDepositForm((prevForm) => ({
                ...prevForm,
                [name]: value
            }));
        }
    };

    const onDateChange = (date) => {
        setDepositForm((prevForm) => ({
            ...prevForm,
            date: date
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setFailedToFetch(false);
        setLoading(true);
        try {
            const { responseStatus, data } = await fetchData('/api/update/deposit', 'PUD', depositForm);

            if (responseStatus === 202) {
                setLoading(false);
                setVisible(false);
                fetchDeposits();
                toast.success("Deposit successfully updated!", {toastId: 'customId'});
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setFailedToFetch(true);
                setLoading(false);
            } else {
                setLoading(false);
                toast.warn(error.message, {toastId: 'customId'});
            }
        }
    };

    return (
        <>
            <FiEdit onClick={showModal} cursor='pointer' size={15} id={`updateDepositModal${deposit.depositId}`} />

            <Modal visible={visible} onClose={closeModal}>
                {loading ? (
                    <div className='loading-indicator'>
                        <FaSpinner className='spinner' />
                    </div>
                ) : failedToFetch ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon' />
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={onSubmit}>
                            <FaSync className='retry-icon' />
                        </button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor='categoryId'>Category: </label>
                            <select className='form-input' name='categoryId' id='updateDepositCategoryInput' value={depositForm.categoryId} onChange={onChange}>
                                {categories && categories.length > 0 && (
                                    categories.map(category => (
                                        <option key={category.categoryId} value={category.categoryId}>{category.categoryName}</option>
                                        ))
                                )}
                            </select>

                            <label className="form-label" htmlFor="date">Date: </label>
                            <DatePicker className="form-input" selected={depositForm.date} onChange={onDateChange} name="date" id="updateDepositDateInput" />

                            <label className="form-label" htmlFor="description">Description: </label>
                            <input className="form-input" type="text" name="description" id="updateDepositDescriptionInput" value={depositForm.description} onChange={onChange} />

                            <label className="form-label" htmlFor="amount">Amount: </label>
                            <input className="form-input" type="number" name="amount" id="updateDepositAmountInput" value={depositForm.amount} onChange={onChange} />

                            <button className='form-btn-1' type='submit' id='updateDepositButton'>Update Deposit</button>
                        </div>
                    </form>
                )}
            </Modal>
        </>
    );
}