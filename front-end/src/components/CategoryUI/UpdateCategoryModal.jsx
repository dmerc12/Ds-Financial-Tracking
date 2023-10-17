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
        setCategoryForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setFailedToFetch(false);
        setLoading(true);
        try {
            const { responseStatus, data } = await fetchData('/api/update/category', 'PUT', categoryForm);

            if (responseStatus === 202) {
                setLoading(false);
                setVisible(false);
                fetchCategories();
                toast.success("Category successfully updated!", {toastId: 'customId'});
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
            <FiEdit onClick={showModal} cursor='pointer' size={15} id={`updateCategoryModal${category.categoryId}`} />

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
                            <label className='form-label' htmlFor='categoryId'>Category ID: </label>
                            <input className='form-input' type='number' name='categoryId' disabled value={categoryForm.categoryId} />
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor='categoryName'>Category Name: </label>
                            <input className='form-input' type='text' name='categoryName' id='updateCategoryNameInput' value={categoryForm.categoryName} onChange={onChange} />
                        </div>

                        <button className='form-btn-1' type='submit' id='updateCategoryButton'>Update Category</button>
                    </form>
                )}
            </Modal>
        </>
    );
}