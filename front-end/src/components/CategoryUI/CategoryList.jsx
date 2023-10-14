import { CreateCategoryModal } from "./CreateCategoryModal";
import { UpdateCategoryModal } from "./UpdateCategoryModal";
import { DeleteCategoryModal } from "./DeleteCategoryModal";
import { useFetch } from "../../hooks/useFetch";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaSpinner, FaSync } from "react-icons/fa"; 
import { AiOutlineExclamationCircle } from "react-icons/ai";
import { toast } from "react-toastify";

export const CategoryList = () => {
    const [categories, setCategories] = useState([]);
    const [listState, setListState] = useState({
        loading: false,
        failedToFetch: false
    });

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const goBack = () => {
        navigate('/home');
        setListState.failedToFetch(false);
    };
    
    let categoryRows = [];

    const fetchCategories = async () => {
        setListState({
            loading: true,
            failedToFetch: false
        });
        try {
            const { responseStatus, data } = await fetchData('/api/get/all/categories', 'GET', {});

            if (responseStatus === 200) {
                setCategories(data);
                setListState.loading(false);
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back end server, please try again!");
            }
        } catch (error) {
            if (error.message === 'Failed to fetch') {
                setListState({
                    loading: false,
                    failedToFetch: true
                });
                } else {
                setListState.loading(false);
                toast.warn(error.message, {toastId: 'customId'});
                }
        }
    };

    useEffect(() => {
        fetchCategories();
    }, []);

    if (categories.length > 0) {
        for (let i=0; 9 < categories.length; i++) {
            const category = categories[i];
            categoryRows.push(
                <tr key={category.categoryId}>
                    <td className="table-data">{category.categoryName}</td>
                    <td className="table-data">
                        <UpdateCategoryModal category={category} fetchCategories={fetchCategories} />
                        <DeleteCategoryModal category={category} fetchCategories={fetchCategories} />
                    </td>
                </tr>
            )
        }
    };

    return (
        <>
            <CreateCategoryModal category={category} fetchCategories={fetchCategories} />
            {listState.loading ? (
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
}