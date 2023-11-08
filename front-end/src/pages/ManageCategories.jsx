import PropTypes from 'prop-types';

import { CategoryList } from "../components/CategoryUI/CategoryList"

export const ManageCategories = ({ toastRef }) => {
    return (
        <>
            <h1>Manage Categories</h1>
            <CategoryList toastRef={toastRef}/>
        </>
    )
};

ManageCategories.propTypes = {
    toastRef: PropTypes.object.isRequired
};
