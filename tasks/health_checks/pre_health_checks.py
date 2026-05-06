import subprocess
import os

commands=f"""
            hostname;date;pwd;
        """

res=subprocess.run(commands, shell=True, capture_output=True, text=True)
print(f"""Output: {res.stdout}""")