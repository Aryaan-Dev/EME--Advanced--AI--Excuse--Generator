const canvas = document.getElementById("canvasOne");
const ctx = canvas.getContext("2d");

let particlesArray = [];
const numberOfParticles = 140; // Increased for more stars

class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 1.5 + 1; // Slightly larger range for variety
        this.speedX = Math.random() * 0.4 - 0.25; // Slower movement for a calmer effect
        this.speedY = Math.random() * 0.4 - 0.25;
        this.opacity = Math.random() * 0.5 + 0.5; // Opacity between 0.5 and 1 for brightness
        this.glow = Math.random() * 10 + 5; // Random glow intensity
    }
    update() {
        this.x += this.speedX;
        this.y += this.speedY;
        if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
        if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
        ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
        ctx.shadowBlur = this.glow;
        ctx.shadowColor = "rgba(198, 223, 251, 0.8)"; // White glow for stars
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0; // Reset shadowBlur to avoid affecting other drawings
    }
}

function init() {
    particlesArray = [];
    for (let i = 0; i < numberOfParticles; i++) {
        particlesArray.push(new Particle());
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
        particlesArray[i].draw();
    }
    requestAnimationFrame(animate);
}

// Adjust canvas size to window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

init();
animate();

// Resize canvas when window size changes
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init(); // Reinitialize particles to fit new canvas size
});