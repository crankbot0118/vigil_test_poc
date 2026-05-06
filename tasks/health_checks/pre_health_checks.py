import subprocess
import os
from tasks.utils import shell_run as sr

commands=f"""
            hostname;date;pwd;
        """

runner = sr.shell_run(commands)
print(runner.run_shell_cmd())