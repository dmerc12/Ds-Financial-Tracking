import { Link } from 'react-router-dom';

export const Navbar = () => {
    return (
        <>
            <nav className='navbar'>
                <Link id='homeNav' className='nav-item' to='/home'>Home</Link>
                <Link id='homeNav' className='nav-item' to='/manage/categories'>Manage Categories</Link>
                <Link id='homeNav' className='nav-item' to='/manage/deposits'>Manage Deposits</Link>
                <Link id='homeNav' className='nav-item' to='/manage/expenses'>Manage Expenses</Link>
            </nav>
        </>
    )
}