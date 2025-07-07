function sendMessage() {
    const input = document.getElementById("input");
    const message = input.value;
    if (!message.trim()) return;

    addMessage("user", message);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage("bot", data.reply);
    });
}

function addMessage(sender, text) {
    const messages = document.getElementById("messages");
    const div = document.createElement("div");
    div.className = "message " + sender;
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}
