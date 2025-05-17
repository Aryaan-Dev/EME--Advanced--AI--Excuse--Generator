$(document).ready(function () {
    // Textillate animation for the ask-text
    $(".ask-text").textillate({
        in: { effect: "fadeIn", delay: 100 },
        out: { effect: "fadeOut", delay: 100 },
        loop: true,
    });

    var siriWave;

    function startSiriWave() {
        if (!siriWave) {
            siriWave = new SiriWave({
                container: document.getElementById("siri-container"),
                width: 700,
                height: 200,
                style: "ios9",
                amplitude: 1,
                speed: 0.30,
                autostart: true
            });
        } else {
            siriWave.start();
        }
    }

    // Microphone button click handler
    document.querySelector(".mic-btn").addEventListener("click", function() {
        console.log("Microphone button clicked!");
        startSiriWave();
    });

    // Handle chat submission
    document.querySelector(".chat-btn").addEventListener("click", function () {
        const inputField = document.querySelector("#chat-input");
        const message = inputField.value.trim();
        if (!message) return;

        // Display user message
        const chatContainer = document.querySelector("#chat-container");
        chatContainer.innerHTML += `<div class="user-message">${message}</div>`;
        inputField.value = '';

        // Send message to backend
        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            // Display bot response
            chatContainer.innerHTML += `<div class="bot-message">${data.response}</div>`;
            chatContainer.scrollTop = chatContainer.scrollHeight; // Auto-scroll to bottom
        })
        .catch(error => {
            console.error('Error:', error);
            chatContainer.innerHTML += `<div class="bot-message">Error: Could not get response</div>`;
        });
    });

    // Textillate animation for siri-message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeInUp", sync: true },
        out: { effect: "fadeOutUp", sync: true },
    });

    // Add Enter key support for chat input
    document.querySelector("#chat-input").addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            document.querySelector(".chat-btn").click();
        }
    });

    // Settings button click handler
    document.querySelector(".settings-btn")?.addEventListener("click", function () {
        console.log("Settings button clicked!");
    });
});