import React, { useState, useRef } from 'react';

function App() {
  const [serverResponse, setResponse] = useState("")
  const inputRef = useRef(null);

  const requestOptions = {
    method: 'GET'
  }
  
  function handleKeyDown(e) {
    if (e.key === 'Enter') {
      console.log('You pressed enter key');
      console.log(inputRef.current.value);
      var userInput = inputRef.current.value;
     
      fetch("https://apad-assignment2-rithu.herokuapp.com/api/getter/" + userInput, requestOptions)
      .then(res => res.json())
      .then(data => setResponse(data.output))
    }
  }

  return (
    <div className="App">
      <h4> Type "rithu" or "Rithu" and press enter to get the last name. Any other word should return "user not found" </h4>
      <p> Your input request to server </p>
      <input
            type="text"
            ref={inputRef}
            onKeyDown={handleKeyDown}
      />

      <p> Response from server </p>
      <input
          type="text"
          value={serverResponse}
          readOnly
      />
    </div>
  );
}

export default App;
