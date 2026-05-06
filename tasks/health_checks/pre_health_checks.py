import subprocess
import os
from tasks.utils.shell_run import shell_run as sr

commands=f"""
            hostname;date;pwd;
        """

print(sr.run_shell_cmd(commands))