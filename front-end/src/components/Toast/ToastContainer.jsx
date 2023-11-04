import styles from './styles.module.css';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import { uuid } from '../../../lib/Helpers';
import { useToast } from '../../../hooks/useToast';
import { useToastAutoClose } from '../../../hooks/useToastAutoClose';
import { forwardRef, useImperativeHandle, useState } from 'react';
import { Toast } from './Toast';

export const ToastContainer = forwardRef(function ToastContainer
    ({ autoClose = true, autoCloseTime = 5000 }, ref) {
        const [ toasts, setToasts] = useState([]);
        const { loaded, toastId } = useToast();

        useToastAutoClose({ toasts, setToasts, autoClose, autoCloseTime });

        const removeToast = id => {
            setToasts((toasts) => toasts.filter(toast => toast.id !== id));
        };

        useImperativeHandle(ref, () => ({
            addToast(toast) {
                setToasts((toasts) => [...toasts, { ...toast, id: uuid() }]);
            }
        }));

        return loaded ? ReactDOM.createPortal(
            <div className={styles.toastContainer}>
                {toasts.map(toast => (
                    <Toast key={toast.id} mode={toast.mode} message={toast.message} onClose={() => removeToast(toast.id)} />
                ))}
            </div>,
            document.getElementById(toastId)
        ) : (
            <></>
        )
    }
);

ToastContainer.propTypes = {
    autoClose: PropTypes.bool,
    autoCloseTime: PropTypes.number
};
