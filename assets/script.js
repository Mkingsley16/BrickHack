function handleSubmit(event) {
    event.preventDefault(); // prevent the form from submitting
  
    // get the input value
    const input = document.getElementById('input').value;
  
    // run the algorithm
    const output = encryptWithAES(input);
  
    // display the output
    const outputElement = document.getElementById('output');
    outputElement.innerText = output;
  }
  
  function encryptWithAES(input) {
    // const CryptoJS = require('crypto-js');
    // add your algorithm code here
    const pass = '123';
    return CryptoJS.AES.encrypt(input, pass);
  }
  
  // add an event listener to the form
  const form = document.querySelector('form');
  form.addEventListener('submit', handleSubmit);
  