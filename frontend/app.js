async function runPreHealthCheck() {
  const logBox = document.getElementById('log-output');
  const btn = document.getElementById('run-btn');

  btn.disabled = true;
  btn.textContent = 'Running...';
  logBox.textContent = '';

  const response = await fetch('http://localhost:8000/tasks/pre-health-check/execute', {
    method: 'POST',
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    // SSE lines look like: "data: some text\n\n"
    const lines = chunk.split('\n').filter(l => l.startsWith('data: '));

    for (const line of lines) {
      const text = line.replace('data: ', '');
      if (text === '__DONE__') {
        btn.textContent = 'Run Pre-Health Check';
        btn.disabled = false;
        return;
      }
      logBox.textContent += text + '\n';
      logBox.scrollTop = logBox.scrollHeight; // auto-scroll
    }
  }
}