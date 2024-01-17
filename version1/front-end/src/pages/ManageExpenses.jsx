import PropTypes from 'prop-types';

import { ExpenseList } from '../components';

export const ManageExpenses = ({ toastRef }) => {
    return (
        <>
            <h1>Manage Expenses</h1>
            <ExpenseList toastRef={toastRef}/>
        </>
    )
};

ManageExpenses.propTypes = {
    toastRef: PropTypes.object.isRequired
};
