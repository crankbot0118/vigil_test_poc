import subprocess
import time

class shell_run:
    def __init__(self, cmd):
        self.cmd=cmd

    def run_shell_cmd(self):
        try:
            start_time=time.time()
            res = subprocess.run(
                self.cmd,
                shell=True,
                executable="/bin/bash",
                capture_output=True,
                text=True,
                timeout=300,
                check=True   #auto-raise if returncode != 0
            )
            end_time=time.time()
            print(f"Total Execution time: {end_time-start_time} secs...")
            return res.stdout.strip()

        except Exception as e:
            raise RuntimeError(f"Command failed: {str(e)}")