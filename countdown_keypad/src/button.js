import React, { useState } from 'react';
import './styles/buttonStyle.scss';

function Button({ number, onClick, disabled }) {
    return (
        <div style={{ display: "inline" }}>
            <button label={number.toString()} value={number} onClick={onClick}
                disabled={disabled} className="btnStyle">{number}</button>
        </div>
    );
}

export default Button;