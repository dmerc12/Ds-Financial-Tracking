import PropTypes from 'prop-types';

import { CreateCategoryModal } from "./CreateCategoryModal";
import { UpdateCategoryModal } from "./UpdateCategoryModal";
import { DeleteCategoryModal } from "./DeleteCategoryModal";
import { useFetch } from "../../hooks/useFetch";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaSpinner, FaSync } from "react-icons/fa"; 
import { AiOutlineExclamationCircle } from "react-icons/ai";

export const CategoryList = ({ toastRef }) => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const goBack = () => {
        navigate('/home');
        setFailedToFetch(false);
    };
    
    let categoryRows = [];

    const fetchCategories = async () => {
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/categories', 'GET');

            if (responseStatus === 200) {
                setCategories(data);
                setLoading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setLoading(false);
                setFailedToFetch(true)
                } else {
                setLoading(false);
                toastRef.current.addToast({ mode: 'error', message: error.message});
                }
        }
    };

    useEffect(() => {
        fetchCategories();
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    if (categories.length > 0) {
        for (let i=0; i < categories.length; i++) {
            const category = categories[i];
            categoryRows.push(
                <tr key={category.categoryId}>
                    <td className="table-data">{category.categoryName}</td>
                    <td className="table-data">
                        <UpdateCategoryModal toastRef={toastRef} category={category} fetchCategories={fetchCategories} />
                        <DeleteCategoryModal toastRef={toastRef} category={category} fetchCategories={fetchCategories} />
                    </td>
                </tr>
            )
        }
    }

    return (
        <>
            <CreateCategoryModal toastRef={toastRef} fetchCategories={fetchCategories} />
            {loading ? (
                <div className='loading-indicator'>
                    <FaSpinner className='spinner' />
                </div>
            ) : failedToFetch ? (
                <div className='failed-to-fetch'>
                    <AiOutlineExclamationCircle className='warning-icon'/>
                    <p>Cannot connect to the back end server.</p>
                    <p>Please check your internet connection and try again.</p>
                    <button className='retry-button' onClick={fetchCategories}>
                        <FaSync className='retry-icon'/> Retry
                    </button>
                    <button className='back-button' onClick={goBack}>Go Back</button>
                </div>
            ) : categories.length === 0 ? (
                <div className="empty-list">No categories have been created yet. Click the Add Category button to create a new category.</div>
            ) : (
                <div className="list">
                    <table className="table">
                        <thead>
                            <tr>
                                <th className="table-head">Category Name</th>
                                <th className="table-head">Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                                {categoryRows}
                        </tbody>
                    </table>
                </div>
            )}
        </>
    );
};

CategoryList.propTypes = {
    toastRef: PropTypes.object.isRequired
};
