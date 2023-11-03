import './App.css';
import 'react-datepicker/dist/react-datepicker.css'

import { ToastContainer } from './components/Toast/ToastContainer';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Home } from './pages/Home';
import { ManageCategories } from './pages/ManageCategories';
import { ManageDeposits } from './pages/ManageDeposits';
import { ManageExpenses } from './pages/ManageExpenses';
import { useRef } from 'react';


function App() {
  const toastRef = useRef();

  return (
    <>
      <Navbar toastRef={toastRef}/>

      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path='/manage/categories' element={<ManageCategories toastRef={toastRef}/>} />
          <Route path='/manage/deposits' element={<ManageDeposits toastRef={toastRef}/>} />
          <Route path='/manage/expenses' element={<ManageExpenses toastRef={toastRef}/>} />
        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toastRef} />
    </>
  )
}

export default App
