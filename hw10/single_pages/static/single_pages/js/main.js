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
        const input = document.querySelector("#user-name");
        const name = input.value.trim();

        if (!name) {
            showMessage("이름을 입력해 주세요.", true);
            input.focus();
            return;
        }
        showMessage(`Hello, ${name}! Django 홈페이지에 오신 것을 환영합니다.`);
    });
}
