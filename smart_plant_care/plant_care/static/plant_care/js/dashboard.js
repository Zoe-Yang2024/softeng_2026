document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("sensorChart");
    const dataNode = document.getElementById("sensor-chart-data");
    if (!canvas || !dataNode) return;

    const data = JSON.parse(dataNode.textContent);
    const context = canvas.getContext("2d");
    const tabs = document.querySelectorAll("[data-series]");
    let activeSeries = "moisture";

    const styles = {
        moisture: { color: "#1f6b4f", fill: "rgba(31, 107, 79, .12)", unit: "%" },
        temperature: { color: "#d97b3d", fill: "rgba(217, 123, 61, .12)", unit: "°C" },
        light: { color: "#b28b19", fill: "rgba(210, 174, 54, .15)", unit: " lx" },
    };

    function draw() {
        const ratio = window.devicePixelRatio || 1;
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        canvas.width = width * ratio;
        canvas.height = height * ratio;
        context.setTransform(ratio, 0, 0, ratio, 0, 0);
        context.clearRect(0, 0, width, height);

        const values = data[activeSeries];
        const style = styles[activeSeries];
        const padding = { top: 28, right: 24, bottom: 38, left: 42 };
        const chartWidth = width - padding.left - padding.right;
        const chartHeight = height - padding.top - padding.bottom;
        const min = Math.min(...values) * .9;
        const max = Math.max(...values) * 1.08;
        const x = index => padding.left + (index / (values.length - 1)) * chartWidth;
        const y = value => padding.top + (1 - (value - min) / (max - min || 1)) * chartHeight;

        context.strokeStyle = "#e2e7e2";
        context.lineWidth = 1;
        context.font = "11px Arial";
        context.fillStyle = "#849087";
        context.textAlign = "right";
        for (let line = 0; line <= 4; line += 1) {
            const lineY = padding.top + (line / 4) * chartHeight;
            context.beginPath();
            context.moveTo(padding.left, lineY);
            context.lineTo(width - padding.right, lineY);
            context.stroke();
            const value = max - (line / 4) * (max - min);
            context.fillText(`${Math.round(value)}${style.unit}`, padding.left - 8, lineY + 4);
        }

        context.textAlign = "center";
        data.labels.forEach((label, index) => {
            if (index % 2 === 0 || index === data.labels.length - 1) {
                context.fillText(label, x(index), height - 12);
            }
        });

        context.beginPath();
        values.forEach((value, index) => {
            if (index === 0) context.moveTo(x(index), y(value));
            else context.lineTo(x(index), y(value));
        });
        context.lineTo(x(values.length - 1), padding.top + chartHeight);
        context.lineTo(x(0), padding.top + chartHeight);
        context.closePath();
        context.fillStyle = style.fill;
        context.fill();

        context.beginPath();
        values.forEach((value, index) => {
            if (index === 0) context.moveTo(x(index), y(value));
            else context.lineTo(x(index), y(value));
        });
        context.strokeStyle = style.color;
        context.lineWidth = 3;
        context.lineJoin = "round";
        context.stroke();

        values.forEach((value, index) => {
            context.beginPath();
            context.arc(x(index), y(value), index === values.length - 1 ? 5 : 3, 0, Math.PI * 2);
            context.fillStyle = index === values.length - 1 ? "#ffffff" : style.color;
            context.fill();
            context.strokeStyle = style.color;
            context.lineWidth = 2;
            context.stroke();
        });
    }

    tabs.forEach(tab => tab.addEventListener("click", () => {
        tabs.forEach(item => item.classList.remove("active"));
        tab.classList.add("active");
        activeSeries = tab.dataset.series;
        draw();
    }));

    window.addEventListener("resize", draw);
    draw();
});
