import { useEffect, useState } from "react";
import { useFetch  } from "../../hooks/useFetch";
import { toast } from "react-toastify";
import { FaSpinner, FaSync } from "react-icons/fa";
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { Modal } from "../Modal";
import DatePicker from "react-datepicker";

// eslint-disable-next-line react/prop-types
export const CreateDepositModal = ({ fetchDeposits }) => {
    const [depositForm, setDepositForm] = useState({
        categoryId: Number(0),
        date: '',
        description: '',
        amount: Number(0.00)
    });
    const [categories, setCategories] = useState([]);
    const [visible, setVisible] = useState(false);
    const [loading, setLoading] = useState(false);
    const [failedToFetchCategories, setFailedToFetchCategories] = useState(false);
    const [failedToFetchSubmission, setFailedToFetchSubmission] = useState(false);


    const { fetchData } = useFetch();

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        setFailedToFetchCategories(false);
        setFailedToFetchSubmission(false);
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

    const fetchCategories = async () => {
        setLoading(true);
        setFailedToFetchCategories(false);
        setFailedToFetchSubmission(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/categories', 'GET');

            if (responseStatus === 200) {
                setCategories(data);
                setDepositForm((prevForm) => ({
                    ...prevForm,
                    categoryId: Number(data[0].categoryId)
                }));
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetchCategories(true);
             } else {
                setLoading(false);
                toast.warn(error.message, {toastId: 'customId'});
             }
        }
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetchCategories(false);
        setFailedToFetchSubmission(false);
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
                toast.success("Deposit successfully created!", {toastId: 'customId'});
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetchSubmission(true);
             } else {
                setLoading(false);
                toast.warn(error.message, {toastId: 'customId'});
             }
        }
    };

    useEffect(() => {
        fetchCategories();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

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
            ) : failedToFetchSubmission ? (
               <div className='failed-to-fetch'>
                  <AiOutlineExclamationCircle className='warning-icon' />
                  <p>Cannot connect to the back end server.</p>
                  <p>Please check your internet connection and try again.</p>
                  <button className='retry-button' onClick={onSubmit}>
                     <FaSync className='retry-icon' />
                  </button>
                  <button className='back-button' onClick={goBack}>Go Back</button>
               </div>
            ) : failedToFetchCategories ? (
                <div className='failed-to-fetch'>
                  <AiOutlineExclamationCircle className='warning-icon' />
                  <p>Cannot connect to the back end server.</p>
                  <p>Please check your internet connection and try again.</p>
                  <button className='retry-button' onClick={fetchCategories}>
                     <FaSync className='retry-icon' />
                  </button>
                  <button className='back-button' onClick={goBack}>Go Back</button>
               </div>
            ) : (
               <form className='form' onSubmit={onSubmit}>
                    <div className='form-field'>
                        <label className='form-label' htmlFor='categoryId'>Category: </label>
                        <select className='form-input' name='categoryId' id='createDepositCategoryInput' value={depositForm.categoryId} onChange={onChange}>
                            {categories && categories.length > 0 && (
                                categories.map(category => (
                                    <option key={category.categoryId} value={category.categoryId}>{category.categoryName}</option>
                                ))
                            )}
                        </select>

                        <label className="form-label" htmlFor="date">Date: </label>
                        <DatePicker className="form-input" selected={depositForm.date} onChange={onDateChange} name="date" id="createDepositDateInput" />

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
}
