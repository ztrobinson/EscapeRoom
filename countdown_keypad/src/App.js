import React, { useCallback, useState } from 'react';
import logo from './logo.svg';
// import './App.css';
import Button from './button.js';
import './styles/app.scss';
// import './styles/fonts/digitaldream/DIGITALDREAM.tff';
import Timer from 'react-compound-timer';


function App() {
  const [guess, setGuess] = useState([]);
  const [correctValue, setCorrectValue] = useState([1,2,3,4]);
  const [isSuccess, setIsSuccess] = useState(false);
  const [btnDisabled, setBtnDisabled] = useState(false);


  function appendNumber(number){
    // var newValue = parseInt(value.toString() + number.toString());
    var newVal = guess.concat(number);
    setGuess(newVal);
    guess.length + 1 < correctValue.length ? setBtnDisabled(false) : setBtnDisabled(true);
    isGuessCorrect(newVal) ? setIsSuccess(true) : setIsSuccess(false);
  }

  function isGuessCorrect(val){
    return JSON.stringify(val) === JSON.stringify(correctValue) ? true : false;
  }

  function clearValue(){
    setGuess([]);
    setIsSuccess(false);
    setBtnDisabled(false);
  }

  return (
    <div className="App" >
      <header className="App-header">
        <div background="dark-1" align="center" style={{margin: "auto"}, {width: "100%"}}>
        {isSuccess ? <h1 className="successHeading">Success!!!!</h1>
        :   
      <Timer      
        initialTime={1000 * 60 * 15}
        direction="backward"
        >
        <h1 className="digitalClock digitalFont">
          <Timer.Minutes />:<Timer.Seconds />
        </h1>
      </Timer>
}
      <br/>
        <div className="answerSection">
          {correctValue.map((answer, index) => (
            <div className="answerBox">{typeof guess[index] === 'undefined' ? 'X' : guess[index].toString()}</div>
            ))}
        </div>

        </div>
        <div className="keypadContainer">

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
        <br/>
        <br/>
        <div style={{textAlign: "center"}}>
          <button onClick={clearValue} style={{ backgroundColor: "red"}}>Clear</button>
        </div>
      </header>
    </div>
  );
}

export default App;