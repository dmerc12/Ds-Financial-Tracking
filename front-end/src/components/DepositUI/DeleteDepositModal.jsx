import PropTypes from 'prop-types';

import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { FiTrash2 } from 'react-icons/fi';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const DeleteDepositModal = ({ toastRef, deposit, fetchDeposits}) => {
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

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/delete/deposit', 'DELETE', {depositId: deposit.depositId});

            if (responseStatus === 202) {
                setLoading(false);
                setVisible(false);
                fetchDeposits();
                toastRef.current.addToast({ mode: 'success', message: 'Deposit successfully deleted!'});
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
                toastRef.current.addToast({ mode: 'error', message: error.message});
            }
        }
    };

    return (
        <>
            <FiTrash2 onClick={showModal} id={`deleteDepositModal${deposit.depositId}`} cursor='pointer' size={15} />

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
                        <button className='back-button' onClick={goBack}>GoBack</button>
                    </div>
                ) : (
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor='depositId'>Deposit ID: </label>
                            <input className='form-input' name='depositId' value={deposit.depositId} disabled type='number' />
                        </div>

                        <div className='form-field'>
                            <label className='form-label'>Are you sure you want to delete this deposit?</label>
                        </div>

                        <button className='form-btn-1' type='submit' id='deleteDepositButton'>Delete Deposit</button>
                    </form>
                )}
            </Modal>
        </>
    );
};

DeleteDepositModal.propTypes = {
    toastRef: PropTypes.object.isRequired,
    deposit: PropTypes.object.isRequired,
    fetchDeposits: PropTypes.func.isRequired,
};
