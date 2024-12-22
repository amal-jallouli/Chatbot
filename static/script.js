function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Display the user message in the chat log
    const chatLog = document.getElementById("chat-log");
    chatLog.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

    // Clear the input field
    document.getElementById("user-input").value = "";

    // Send the message to the server
    fetch('/chatbot/respond', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const chatbotMessage = data.response;
        chatLog.innerHTML += `<div><strong>Chatbot:</strong> ${chatbotMessage}</div>`;
        chatLog.scrollTop = chatLog.scrollHeight; // Scroll to the bottom
    })
    .catch(error => {
        chatLog.innerHTML += `<div><strong>Error:</strong> ${error}</div>`;
    });
}
