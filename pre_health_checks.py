from run_shell_cmd import shell_run as sr

command = r'''
echo "=================================================="
echo "              SYSTEM HEALTH REPORT"
echo "=================================================="

echo
echo "================ HOST INFO ======================="
printf "%-20s : %s\n" "Hostname" "$(hostname)"
printf "%-20s : %s\n" "Date" "$(date)"
printf "%-20s : %s\n" "Working Directory" "$(pwd)"

echo
echo "================ UPTIME =========================="
uptime

echo
echo "================ CPU SNAPSHOT ===================="
top -bn1 | head -15

echo
echo "================ MEMORY USAGE ===================="
free -h

echo
echo "================ TOP MEMORY PROCESSES ============"
printf "%-10s %-10s %-10s %-10s %-40s\n" "USER" "PID" "%CPU" "%MEM" "COMMAND"
ps aux --sort=-%mem | awk 'NR==1 || NR<=6 {printf "%-10s %-10s %-10s %-10s %-40s\n",$1,$2,$3,$4,$11}'

echo
echo "================ DISK USAGE ======================"
df -h | awk 'NR==1 || /^\/dev/'

echo
echo "================ NETWORK CONNECTIONS ============="
ss -tulnp | head -15

echo
echo "================ FAILED SERVICES ================="
systemctl --failed

echo
echo "=================================================="
echo "            END OF HEALTH REPORT"
echo "=================================================="
'''

runner = sr(command)
print(runner.run_shell_cmd())
