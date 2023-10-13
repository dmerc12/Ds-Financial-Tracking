import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const CreateCategoryModal = ({ fetchCategories }) => {
   const [categoryForm, setCategoryForm] = useState({categoryName: ''});
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
         const { responseStatus, data } = await fetchData('/api/create/category', 'POST', categoryForm);

         if (responseStatus === 201) {
            setCategoryForm({categoryName: ''});
            setModalState({
               failedToFetch: false,
               loading: false,
               visible: false
            });
            fetchCategories();
            toast.success("Category successfully created!", {toastId: 'customId'});
         } else if (responseStatus === 400) {
            throw new Error(`${data.message}`);
         } else {
            throw new Error("Cannot connect to the back end server, please try again!");
         }
      } catch (error) {
         if (error.message === 'Failed to fetch') {
            setModalState((prevState) => ({
               ...prevState,
               failedToFetch: true,
               loading: false
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
            <button onClick={showModal} className='action-btn' id='createCategoryModal'>Create Category</button>
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
                  <button className='back-button' onClick={goBack}>Go Back</button>
               </div>
            ) : (
               <form className='form' onSubmit={onSubmit}>
                  <div className='form-field'>
                     <label className='form-label' htmlFor='categoryName'>Category Name: </label>
                     <input className='form-input' type='text' name='categoryName' id='newCategoryName' value={categoryForm.categoryName} onChange={event => setCategoryForm.categoryName(event.target.value)} />

                     <button className='form-btn-1' type='submit' id='createCategoryButton'>Create Category</button>
                  </div>
               </form>
            )}
         </Modal>
      </>
   );
}