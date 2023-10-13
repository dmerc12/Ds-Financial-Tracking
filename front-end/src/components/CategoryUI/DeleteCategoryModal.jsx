import { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { toast } from 'react-toastify';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { FiTrash2 } from 'react-icons/fi';
import { AiOutlineExclamationCircle } from 'react-icons/ai';
import { Modal } from '../Modal';

export const DeleteCategoryModal = ({ category, fetchCategories }) => {
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
         const { responseStatus, data } = await fetchData('/api/delete/category', 'DELETE', {categoryId: category.categoryId});

         if (responseStatus === 202) {
            setModalState((prevState) => ({
               ...prevState,
               loading: false,
               visible: false
            }));
            fetchCategories();
            toast.success("Category successfully deleted!", {toastId: 'customId'});
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
         <FiTrash2 onClick={showModal} id={`deleteCategoryModal${category.categoryId}`} cursor='pointer' size={15}/>

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
                  <button className='back-button' onClick={goBack}>GoBack</button>
               </div>
            ) : (
               <form className='form' onSubmit={onSubmit}>
                  <div className='form-field'>
                     <label className='form-label'>Are you sure?</label>
                  </div>

                  <button className='form-btn-1' type='submit' id='deleteCategoryButton'>Delete Category</button>
               </form>
            )}
         </Modal>
      </>
   );
}