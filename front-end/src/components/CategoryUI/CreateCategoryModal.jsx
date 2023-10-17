import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

// eslint-disable-next-line react/prop-types
export const CreateCategoryModal = ({ fetchCategories }) => {
   const [categoryForm, setCategoryForm] = useState({categoryName: ''});
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
      }))
   };

   const onSubmit = async (event) => {
      event.preventDefault();
      setLoading(true);
      setFailedToFetch(false);
      try {
         const { responseStatus, data } = await fetchData('/api/create/category', 'POST', categoryForm);

         if (responseStatus === 201) {
            setCategoryForm({categoryName: ''});
            setVisible(false);
            setLoading(false);
            fetchCategories();
            toast.success("Category successfully created!", {toastId: 'customId'});
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
            toast.warn(error.message, {toastId: 'customId'});
         }
      }
   };

   return (
      <>
         <div className='component'>
            <button onClick={showModal} className='action-btn' id='createCategoryModal'>Create Category</button>
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
                     <label className='form-label' htmlFor='categoryName'>Category Name: </label>
                     <input className='form-input' type='text' name='categoryName' id='createCategoryNameInput' value={categoryForm.categoryName} onChange={onChange} />

                     <button className='form-btn-1' type='submit' id='createCategoryButton'>Create Category</button>
                  </div>
               </form>
            )}
         </Modal>
      </>
   );
}