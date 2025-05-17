$(document).ready(function () {
    // Textillate animation for the ask-text
    $('.ask-text').textillate({ in: { effect: 'fadeIn' } });

    // Reference to the chat input field
    const chatInput = $('#chat-input');
    if (chatInput.length) {
        // Handle chat submission on Enter key press
        chatInput.keypress(function (e) {
            if (e.which === 13) {
                e.preventDefault();
                sendMessage();
            }
        });
    } else {
        console.error('Element with ID "chat-input" not found in the DOM.');
    }

    // Function to send a message
    function sendMessage() {
        const userInput = $('#chat-input').val().trim();
        if (!userInput) return;

        // Append user message to the chat container
        $('#chat-container').append('<div class="user-message">' + userInput + '</div>');
        $('#chat-input').val(''); // Clear the input field

        // Send the message to the backend
        $.ajax({
            url: '/chat',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: userInput }),
            success: function (response) {
                // Append bot response to the chat container
                $('#chat-container').append('<div class="bot-message">' + response.answer + '</div>');
                // Auto-scroll to the bottom of the chat container
                $('#chat-container').scrollTop($('#chat-container')[0].scrollHeight);
            },
            error: function () {
                // Append error message to the chat container
                $('#chat-container').append('<div class="bot-message">Error: Could not get a response.</div>');
            }
        });
    }
});