import PropTypes from 'prop-types';

import { useState } from 'react';
import { useFetch  } from '../../hooks';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const CreateDepositModal = ({ toastRef, categories, fetchDeposits }) => {
    const [depositForm, setDepositForm] = useState({
        categoryId: 0,
        date: '',
        description: '',
        amount: Number(0.00)
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
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/create/deposit', 'POST', depositForm);

            if (responseStatus === 201) {
                setDepositForm({
                    categoryId: Number(0),
                    date: '',
                    description: '',
                    amount: Number(0.00)
                });
                setVisible(false);
                setLoading(false);
                fetchDeposits();
                toastRef.current.addToast({ mode: 'success', message: 'Deposit successfully created!'});
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetch(true);
            } else {
                setLoading(false);
                toastRef.current.addToast({ mode: 'error', message: error.message});
            }
        }
    };

    return (
        <>
            <div className='component'>
                <button onClick={showModal} className='action-btn' id='createDepositModal'>Create Deposit</button>
            </div>

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
                            <select className='form-input' name='categoryId' id='createDepositCategoryInput' value={depositForm.categoryId} onChange={onChange}>
                                <option value={0}>Please choose a category below</option>
                                {categories && categories.length > 0 && (
                                    categories.map(category => (
                                        <option key={category.categoryId} value={category.categoryId}>{category.categoryName}</option>
                                        ))
                                )}
                            </select>

                            <label className="form-label" htmlFor="date">Date: </label>
                            <input className="form-input" type='date' value={depositForm.date} onChange={onDateChange} name="date" id="createDepositDateInput" />

                            <label className="form-label" htmlFor="description">Description: </label>
                            <input className="form-input" type="text" name="description" id="createDepositDescriptionInput" value={depositForm.description} onChange={onChange} />

                            <label className="form-label" htmlFor="amount">Amount: </label>
                            <input className="form-input" type="number" name="amount" id="createDepositAmountInput" value={depositForm.amount} onChange={onChange} />

                            <button className='form-btn-1' type='submit' id='createDepositButton'>Create Deposit</button>
                        </div>
                    </form>
                )}
            </Modal>
        </>
    )
};

CreateDepositModal.propTypes = {
    toastRef: PropTypes.object.isRequired,
    categories: PropTypes.arrayOf(PropTypes.object).isRequired,
    fetchDeposits: PropTypes.func.isRequired
};
