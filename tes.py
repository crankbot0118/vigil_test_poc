from run_shell_cmd import shell_run as sr

command=f"""
        hostname;date;pwd;
        uptime;
        top -bn1 | head -20;
        free -h
        ps aux --sort=-%mem | head
        """

runner = sr(command)
print(runner.run_shell_cmd())
