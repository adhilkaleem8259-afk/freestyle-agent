const taskList = document.getElementById("task-list");
const logList = document.getElementById("log-list");
const taskForm = document.getElementById("task-form");
const clearLogsBtn = document.getElementById("clear-logs");

// Fetch tasks from backend
async function fetchTasks() {
    const res = await fetch("/tasks");
    const tasks = await res.json();
    taskList.innerHTML = "";
    tasks.forEach((t, idx) => {
        const li = document.createElement("li");
        li.textContent = `${idx + 1}. ${t.task} [Agent: ${t.agent || "Unassigned"}]`;
        taskList.appendChild(li);
    });
    // Auto-scroll tasks
    taskList.parentElement.scrollTop = taskList.parentElement.scrollHeight;
}

// Fetch logs from backend
async function fetchLogs() {
    const res = await fetch("/logs");
    const data = await res.json();
    logList.innerHTML = "";
    data.logs.forEach(line => {
        const li = document.createElement("li");
        li.textContent = line;
        logList.appendChild(li);
    });
    // Auto-scroll logs
    logList.parentElement.scrollTop = logList.parentElement.scrollHeight;
}

// Add new task
taskForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const taskInput = document.getElementById("task-input");
    if (!taskInput.value.trim()) return;
    await fetch("/add_task", { method: "POST", body: new URLSearchParams({ task: taskInput.value.trim() }) });
    taskInput.value = "";
    await fetchTasks();
    await fetchLogs();
});

// Clear logs
clearLogsBtn.addEventListener("click", async () => {
    await fetch("/clear_logs", { method: "POST" });
    await fetchLogs();
});

// Update tasks & logs every second
setInterval(async () => { await fetchTasks(); await fetchLogs(); }, 1000);

fetchTasks();
fetchLogs();
