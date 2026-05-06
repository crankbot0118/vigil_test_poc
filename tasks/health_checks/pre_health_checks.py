import subprocess
import os
from tasks.utils.shell_run import shell_run as sr

commands=f"""
            hostname;date;pwd;
        """

runner = sr(commands)
print(runner.run_shell_cmd())