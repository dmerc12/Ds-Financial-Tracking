import './App.css';
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Home } from './pages/Home';
import { ManageCategories } from './pages/ManageCategories';
import { ManageDeposits } from './pages/ManageDeposits';
import { ManageExpenses } from './pages/ManageExpenses';

function App() {

  return (
    <>
      <Navbar />

      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path='/manage/categories' element={<ManageCategories />} />
          <Route path='/manage/deposits' element={<ManageDeposits />} />
          <Route path='/manage/expenses' element={<ManageExpenses />} />
        </Routes>
      </BrowserRouter>

      <ToastContainer position='top-center' newestOnTop autoClose={3000} hideProgressBar theme='colored' limit={1} closeOnClick />
    </>
  )
}

export default App
