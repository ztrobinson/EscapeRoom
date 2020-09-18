import React, { useCallback, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Button from './button.js';

function App() {
  const [value, setValue] = useState(0);
  const [correctValue, setCorrectValue] = useState(1234);
  const [isSuccess, setIsSuccess] = useState(false);

  function appendNumber(number){
    var newValue = parseInt(value.toString() + number.toString());
    setValue(newValue);
    if (newValue == correctValue){
      setIsSuccess(true);
    } else {
      setIsSuccess(false);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {isSuccess ? <h1>Success!!!!!!!!!!!!!!</h1> : <h1>Some Value = {value}</h1>}
        <Button number={0} onClick={() => appendNumber(0)} />
        <Button number={1} onClick={() => appendNumber(1)} />
        <Button number={2} onClick={() => appendNumber(2)} />
        <Button number={3} onClick={() => appendNumber(3)} />
        <Button number={4} onClick={() => appendNumber(4)} />
        <Button number={5} onClick={() => appendNumber(5)} />
        <Button number={6} onClick={() => appendNumber(6)} />
        <Button number={7} onClick={() => appendNumber(7)} />
        <Button number={8} onClick={() => appendNumber(8)} />
        <Button number={9} onClick={() => appendNumber(9)} />
      </header>
    </div>
  );
}

export default App;
