# pip install fastapi uvicorn paramiko

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import paramiko
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Config (move to .env later) ---
SSH_HOST = "54.80.214.20"
SSH_PORT = 22
SSH_USER = "ec2-user"
SSH_KEY  = "/home/ec2-user/vigil_test_poc/key.ppk"   # or use SSH_PASS

# Commands your pre-health check runs
HEALTH_CHECK_COMMANDS = [
    "echo '>>> Checking uptime'",
    "uptime",
    "echo '>>> Checking disk'",
    "df -h /",
    "echo '>>> Checking memory'",
    "free -m",
    "echo '>>> Checking CPU load'",
    "top -bn1 | grep 'load average'",
    "echo '>>> Done'",
]

def stream_health_check():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        yield "data: Connecting to host...\n\n"
        client.connect(
            hostname=SSH_HOST,
            port=SSH_PORT,
            username=SSH_USER,
            key_filename=SSH_KEY,     # swap for password= if needed
            timeout=10,
        )
        yield "data: Connected.\n\n"

        for cmd in HEALTH_CHECK_COMMANDS:
            stdin, stdout, stderr = client.exec_command(cmd)

            for line in stdout:
                yield f"data: {line.rstrip()}\n\n"
            for line in stderr:
                yield f"data: [ERR] {line.rstrip()}\n\n"

        yield "data: __DONE__\n\n"

    except Exception as e:
        yield f"data: [FATAL] {str(e)}\n\n"
        yield "data: __DONE__\n\n"
    finally:
        client.close()


@app.post("/tasks/pre-health-check/execute")
def execute_pre_health_check():
    return StreamingResponse(
        stream_health_check(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )