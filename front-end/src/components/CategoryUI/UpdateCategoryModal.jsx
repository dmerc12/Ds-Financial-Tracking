import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const UpdateCategoryModal = ({ category, fetchCategories }) => {
    const [categoryForm, setCategoryForm] = useState({
        categoryId: category.categoryId,
        categoryName: category.categoryName
    });
    const [modalState, setModalState] = useState({
        loading: false,
        failedToFetch: false,
        visible: false
    });

    const { fetchData } = useFetch();

    const showModal = () => {
        setModalState.visible(true);
    };

    const closeModal = () => {
        setModalState.visible(false);
    };

    const goBack = () => {
        setModalState.failedToFetch(false);
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setModalState((prevState) => ({
            ...prevState,
            loading: true,
            failedToFetch: false
        }));
        try {
            
        } catch (error) {
            if (error.message === 'Failed to fetch') {
            setModalState((prevState) => ({
                ...prevState,
                loading: false,
                failedToFetch: true
            }));
            } else {
            setModalState.loading(false);
            toast.warn(error.message, {toastId: 'customId'});
            }
        }
   };

   return (
        <>
            <div className='component'>
                <button onClick={showModal} className='action-btn' id=''></button>
            </div>

            <Modal visible={visible} onClose={closeModal}>
                {modalState.loading ? (
                <div className='loading-indicator'>
                    <FaSpinner className='spinner' />
                </div>
                ) : modalState.failedToFetch ? (
                <div className='failed-to-fetch'>
                    <AiOutlineExclamationCircle className='warning-icon' />
                    <p>Cannot connect to the back end server.</p>
                    <p>Please check your internet connection and try again.</p>
                    <button className='retry-button' onClick={onSubmit}>
                        <FaSync className='retry-icon' />
                    </button>
                </div>
                ) : (
                
                )}
            </Modal>
        </>
    );
}