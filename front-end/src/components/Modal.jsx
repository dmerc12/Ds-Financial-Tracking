export const Modal = ({ visible, onClose, children }) => {
    if (!visible) return null;

    const handleClose = (event) => {
        const targetElement = event.target;
        if (targetElement.id === "wrapper") onClose();
    }

    return (
        <>
            <div className="modal-exterior-wrapper" id="wrapper" onClick={handleClose}>
                <div className="modal-interior-wrapper">
                    <button className="close-button" onclick={() => onClose()}>Close</button>
                    <div className="modal">
                        {children}
                    </div>
                </div>
            </div>
        </>
    )
}