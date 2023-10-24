import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FiEdit } from 'react-icons/fi';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const UpdateDepositModal = ({ deposit, fetchDeposits }) => {
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
        setDepositForm({
            
        })
    }

    return (
        <>
        
        </>
    );
}