import React, { useState } from 'react';

function Button({number, onClick}) {
  return (
    <div>
        <button value={number} onClick={onClick} style={{cursor:"pointer"}}>{number}</button>
    </div>
  );
}

export default Button;
