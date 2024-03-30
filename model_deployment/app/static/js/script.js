// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the input values from the form
    let feature1Value = document.getElementById('feature1').value;
    let feature2Value = document.getElementById('feature2').value;

    // Make an AJAX request to send the input data to the server
    // use libraries like Axios or the fetch API to make AJAX requests
    // Example using fetch:
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ feature1: feature1Value, feature2: feature2Value })
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result on the web page
        document.getElementById('prediction-result').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Add event listener to the form for form submission
document.getElementById('prediction-form').addEventListener('submit', handleSubmit);
