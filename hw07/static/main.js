
const welcomeForm = document.querySelector("#welcome-form");


function showMessage(text, isError = false) {
    const messageArea = document.querySelector("#message-area");
    const message = document.createElement("p");

    message.className = isError ? "message error" : "message";
    message.textContent = text;
    messageArea.replaceChildren(message);
}


function createBalloons() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        return;
    }

    const colors = ["#ee6c4d", "#4caf75", "#5085d8", "#e7b34a", "#b574cf"];

    for (let index = 0; index < 18; index += 1) {
        const balloon = document.createElement("span");
        const size = Math.random() * 18 + 20;

        balloon.className = "balloon";
        balloon.setAttribute("aria-hidden", "true");
        balloon.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        balloon.style.color = balloon.style.backgroundColor;
        balloon.style.left = `${Math.random() * 100}vw`;
        balloon.style.width = `${size}px`;
        balloon.style.height = `${size * 1.18}px`;
        balloon.style.animationDelay = `${Math.random() * 0.8}s`;
        document.body.appendChild(balloon);

        window.setTimeout(() => balloon.remove(), 5000);
    }
}


if (welcomeForm) {
    welcomeForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const nameInput = document.querySelector("#user-name");
        const name = nameInput.value.trim();

        if (!name) {
            showMessage("이름을 입력해 주세요.", true);
            nameInput.focus();
            return;
        }

        showMessage(`Hello, ${name}! 방문해 주셔서 감사합니다.`);
        createBalloons();
    });
}
