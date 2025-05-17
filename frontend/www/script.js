const canvas = document.getElementById("canvasOne");
const ctx = canvas.getContext("2d");

let particles = [];
const numParticles = 100;

// Create Particles
function createParticles() {
    for (let i = 0; i < numParticles; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 2 + 1,
            speedX: (Math.random() - 0.5) * 2,
            speedY: (Math.random() - 0.5) * 2,
            opacity: Math.random(),
        });
    }
}

// Update & Animate Particles
function updateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach((p) => {
        p.x += p.speedX;
        p.y += p.speedY;

        if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
        if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 0, 255, ${p.opacity})`;
        ctx.fill();
    });

    requestAnimationFrame(updateParticles);
}

// Resize canvas to fit window
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    particles = [];
    createParticles();
}

// Initialize canvas size and particles
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Start animation
updateParticles();

async function sendMessage() {
    const userInput = document.getElementById("chat-input").value;
    if (!userInput.trim()) return;

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    if (data.answer.startsWith("Image generated successfully:")) {
        const imagePath = data.answer.split(":")[1].trim();
        const chatContainer = document.getElementById("chat-container");
        const imgElement = document.createElement("img");
        imgElement.src = `/static/${imagePath}`;
        imgElement.alt = "Generated Image";
        imgElement.style.maxWidth = "100%";
        chatContainer.appendChild(imgElement);
    } else {
        // Handle text responses
        displayMessage(data.answer, "assistant");
    }
}