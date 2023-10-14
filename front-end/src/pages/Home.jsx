import { Link } from 'react-router-dom';

export const Home = () => {
    return (
        <>
            <h1>Welcome!</h1>
            <div className="action-btn-container">
                <Link id='manageCategoriesButton' className='home-nav' to='/manage/categories'>Manage Categories</Link>
                <Link id='manageDepositsButton' className='home-nav' to='/manage/deposits'>Manage Deposits</Link>
                <Link id='manageExpensesButton' className='home-nav' to='/manage/expenses'>Manage Expenses</Link>
            </div>
        </>
    )
}