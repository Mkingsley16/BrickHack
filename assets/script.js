
function handleCeasarSubmit(event) {
    event.preventDefault(); // prevent the form from submitting
  
    // get the input value
    const input = document.getElementById('ceasarinput').value;
    const shift = document.getElementById('ceasarshift').value;

    // run the algorithm
    const output = encryptWithCeasar(input,shift);
    // display the output
    const outputElement = document.getElementById('ceasaroutput');
    outputElement.innerText = output;
  }
  
  function encryptWithCeasar(input,shift) {
      var encryptedMessage = "";
      for (var i = 0; i < input.length; i++) {
        var c = input.charCodeAt(i);
    
        if (c >= 65 && c <= 90) {
          encryptedMessage += String.fromCharCode((c - 65 + shift) % 26 + 65); // uppercase letters
        } else if (c >= 97 && c <= 122) {
          encryptedMessage += String.fromCharCode((c - 97 + shift) % 26 + 97); // lowercase letters
        } else {
          encryptedMessage += message.charAt(i); // non-letter characters
        }
      }
    
      return encryptedMessage;
    }
  
  // add an event listener to the form
  const form = document.querySelector('form');
  form.addEventListener('submit', handleCeasarSubmit);

  

