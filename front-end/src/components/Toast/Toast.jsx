import styles from './styles.module.css';
import PropTypes from 'prop-types';

import { useMemo } from 'react';

export const Toast = ({ mode, onClose, message }) => {
    const classes = useMemo(() => [styles.toast, styles[mode]].join(' '), [mode]);

    return (
        <div onClick={onClose} className={classes}>
            <div id='toast' className={styles.message}>{message}</div>
        </div>
    )
};

Toast.propTypes = {
    mode: PropTypes.string,
    onClose: PropTypes.func,
    message: PropTypes.string
};
