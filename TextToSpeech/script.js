// Get references to HTML elements
const textInput = document.getElementById('text-input');
const speakButton = document.getElementById('speak-button');

// Initialize the speech synthesis object
const synth = window.speechSynthesis;

// Function to read the text
function speakText() {
    const text = textInput.value;
    if (text !== '') {
        const utterance = new SpeechSynthesisUtterance(text);
        synth.speak(utterance);
    }
}

// Add click event listener to the "Speak" button
speakButton.addEventListener('click', speakText);
