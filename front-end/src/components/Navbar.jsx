import { useNavigate } from "../hooks/useNavigate"

export const Navbar = () => {
    const navigate = useNavigate();

    return (
        <>
            <nav className='navbar'>
                <button id='homeNav' className='nav-item' onClick={() => navigate('/home')}>Home</button>
                <button id='manageCategoriesNav' className='nav-item' onClick={() => navigate('/manage/categories')}>Manage Categories</button>
                <button id='manageDepositsNav' className='nav-item' onClick={() => navigate('/manage/deposits')}>Manage Deposits</button>
                <button id='manageExpensesNav' className='nav-item' onClick={() => navigate('/manage/expenses')}>Manage Expenses</button>
            </nav>
        </>
    )
}