import './App.css';
import 'react-datepicker/dist/react-datepicker.css'

import { useRef } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ToastContainer, Navbar } from './components';
import { Home, ManageCategories, ManageDeposits, ManageExpenses } from './pages';

function App() {
  const toastRef = useRef();

  return (
    <>
      <Navbar />

      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path='/manage/categories' element={<ManageCategories toastRef={toastRef}/>} />
          <Route path='/manage/deposits' element={<ManageDeposits toastRef={toastRef}/>} />
          <Route path='/manage/expenses' element={<ManageExpenses toastRef={toastRef}/>} />
        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toastRef} autoClose autoCloseTime={3000}/>
    </>
  )
}

export default App
