// Connect one HTML form to one result area using AJAX and the Fetch API.
function connectForm(formSelector, resultSelector) {
    const form = document.querySelector(formSelector);
    const result = document.querySelector(resultSelector);

    form.addEventListener("submit", async function (event) {
        event.preventDefault();
        result.innerHTML = "<p class='loading'>계산 중...</p>";

        const query = new URLSearchParams(new FormData(form));

        try {
            const response = await fetch(`${form.action}?${query}`);
            const html = await response.text();
            result.innerHTML = html;
        } catch (error) {
            result.innerHTML = "<p class='result-card error'>서버에 연결할 수 없습니다.</p>";
        }
    });
}


document.addEventListener("DOMContentLoaded", function () {
    connectForm("#gugudan-form", "#gugudan-result");
    connectForm("#bmi-form", "#bmi-result");
});
