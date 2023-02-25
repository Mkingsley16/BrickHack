function handleSubmit(event) {
    event.preventDefault(); // prevent the form from submitting
  
    // get the input value
    const input = document.getElementById('input').value;
  
    // run the algorithm
    const output = myAlgorithm(input);
  
    // display the output
    const outputElement = document.getElementById('output');
    outputElement.innerText = output;
  }
  
  function myAlgorithm(input) {
    // add your algorithm code here
    return btoa(input);
  }
  
  // add an event listener to the form
  const form = document.querySelector('form');
  form.addEventListener('submit', handleSubmit);
  