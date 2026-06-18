const welcomeForm = document.querySelector("#welcome-form");


function showMessage(text, isError = false) {
    const messageArea = document.querySelector("#message-area");
    const message = document.createElement("p");

    message.className = isError ? "message error" : "message";
    message.textContent = text;
    messageArea.replaceChildren(message);
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
    });
}
