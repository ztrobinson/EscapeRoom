import React, { useCallback, useState } from 'react';
import logo from './logo.svg';
// import './App.css';
import Button from './button.js';
import './styles/app.scss';

function App() {
  const [value, setValue] = useState("");
  const [correctValue, setCorrectValue] = useState(1234);
  const [isSuccess, setIsSuccess] = useState(false);
  const [btnDisabled, setBtnDisabled] = useState(false);


  function appendNumber(number){
    var newValue = parseInt(value.toString() + number.toString());
    if (newValue == correctValue){
      setIsSuccess(true);
    } else {
      setIsSuccess(false);
    }
    
    if (newValue.toString().length < correctValue.toString().length){
      setBtnDisabled(false);
    } else {
      setBtnDisabled(true);
    }
    setValue(newValue);
  }

  function clearValue(){
    setValue("");
    setIsSuccess(false);
    setBtnDisabled(false);
  }

  return (
    <div className="App" style={appStyle} >
      <header className="App-header">
        <div background="dark-1" align="center" style={{margin: "auto"}, {width: "100%"}}>
        {isSuccess ? <h1 style={{margin: "auto"}, {width: "100%"}}>Success!!!!!!!!!!!!!!</h1> 
        : <h1 style={{margin: "auto"}, {width: "100%"}} alignSelf="center" textAlign="center">Code: {value}</h1>}
        <div className="answerBox"></div>
        <div className="answerBox"></div>
        <div className="answerBox"></div>
        <div className="answerBox"></div>
        </div>
        <div style={btnContainer}>

          <Button number={1} onClick={() => appendNumber(1)} disabled={btnDisabled} />
          <Button number={2} onClick={() => appendNumber(2)} disabled={btnDisabled} />
          <Button number={3} onClick={() => appendNumber(3)} disabled={btnDisabled} />
          <br/>
          <Button number={4} onClick={() => appendNumber(4)} disabled={btnDisabled} />
          <Button number={5} onClick={() => appendNumber(5)} disabled={btnDisabled} />
          <Button number={6} onClick={() => appendNumber(6)} disabled={btnDisabled} />
          <br/>
          <Button number={7} onClick={() => appendNumber(7)} disabled={btnDisabled} />
          <Button number={8} onClick={() => appendNumber(8)} disabled={btnDisabled} />
          <Button number={9} onClick={() => appendNumber(9)} disabled={btnDisabled} />
          <br/>
          <Button number={0} onClick={() => appendNumber(0)} disabled={btnDisabled} />
          {/* <Button number={"Clear"} onClick={() => clearValue()} disabled={btnDisabled} /> */}
          <br />
        </div>
          <button onClick={clearValue} style={{ backgroundColor: "red"}}>Clear</button>
      </header>
    </div>
  );
}

export default App;

const appStyle = {
  // backgroundColor: "gray" 
}
const btnContainer = {
  textAlign: "center"
}