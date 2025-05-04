#!/bin/bash

system_info() {
  # echo "===== System Information ====="

  # Uptime
  echo -e "\n⏱️ System Uptime:"
  uptime -p

  # Available Memory
  echo -e " ${Green}\n🧠 Available Memory:"
  free -h | awk '/^Mem:/ {print "Available: " $7 " / Total: " $2}'

  # Disk Usage
  echo -e "\n💾 Disk Usage Statistics:"
  df -h --total | awk 'NR==1 || /total/'

  # Number of Running Processes
  echo -e "\n⚙️ Number of Running Processes:"
  ps -e --no-headers | wc -l

  # CPU Info
  echo -e "\n🧠 CPU Info:"
  lscpu | grep -E '^Model name|^CPU\(s\)|^Thread|^Core'

  # # Top 5 Processes by CPU Usage
  # echo -e "\n🔥 Top 5 Processes by CPU Usage:"
  # ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6

  # # Top 5 Processes by Memory Usage
  # echo -e "\n💡 Top 5 Processes by Memory Usage:"
  # ps -eo pid,comm,%cpu,%mem --sort=-%mem | head -n 6
}

