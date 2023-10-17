/* eslint-disable react/prop-types */
import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FiEdit } from 'react-icons/fi';
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
            const { responseStatus, data } = await fetchData('/api/update/category', 'PUT', categoryForm);

            if (responseStatus === 202) {
                setModalState({
                    failedToFetch: false,
                    loading: false,
                    visible: false
                });
                fetchCategories();
                toast.success("Category successfully updated!", {toastId: 'customId'});
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
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
            <FiEdit onClick={showModal} cursor='pointer' size={15} id={`updateCategoryModal${category.categoryId}`} />

            <Modal visible={modalState.visible} onClose={closeModal}>
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
                    <button className='back-button' onClick={goBack}>Go Back</button>
                </div>
                ) : (
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor='categoryId'>Category ID: </label>
                            <input className='form-input' type='number' name='categoryId' disabled value={categoryForm.categoryId} />
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor='categoryName'>Category Name: </label>
                            <input className='form-input' type='text' name='categoryName' id='updateCategoryNameInput' value={categoryForm.categoryName} onChange={event => setCategoryForm.categoryName(event.target.value)} />
                        </div>

                        <button className='form-btn-1' type='submit' id='updateCategoryButton'>Update Category</button>
                    </form>
                )}
            </Modal>
        </>
    );
}