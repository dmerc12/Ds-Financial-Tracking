import PropTypes from 'prop-types';

import { DepositList } from '../components';

export const ManageDeposits = ({ toastRef }) => {
    return (
        <>
            <h1>Manage Deposits</h1>
            <DepositList toastRef={toastRef}/>
        </>
    )
};

ManageDeposits.propTypes = {
    toastRef: PropTypes.object.isRequired
};
