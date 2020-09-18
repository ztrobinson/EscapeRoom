import React, { useState } from 'react';

function Button({number, onClick, disabled}) {
  return (
    <div>
        <button value={number} onClick={onClick} disabled={disabled} style={{cursor:"pointer"}}>{number}</button>
    </div>
  );
}

export default Button;
