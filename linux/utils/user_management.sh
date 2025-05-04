#!/bin/bash

user_management() {
  echo "===== 🧑‍💻 User Management Information ====="

  # Currently logged-in users
  echo -e "\n👥 Logged-in Users:"
  who

  # Total number of users
  echo -e "\n🔢 Total System Users:"
  getent passwd | wc -l

  # List of users created in the last 7 days
  echo -e "\n🆕 Users Created in the Last 7 Days:"
  sudo awk -F: '{ print $1, $3 }' /etc/passwd | while read user uid; do
    if [[ "$uid" -ge 1000 ]]; then
      home_dir=$(eval echo "~$user")
      if [ -d "$home_dir" ] && [ $(find "$home_dir" -ctime -7 2>/dev/null | wc -l) -gt 0 ]; then
        echo "$user"
      fi
    fi
  done

  # User Shell Usage
  echo -e "\n🐚 Most Common Shells:"
  awk -F: '{ print $7 }' /etc/passwd | sort | uniq -c | sort -nr

  # Last logins using 'last' instead of 'lastlog'
  echo -e "\n🕓 Recent Login Sessions (last 5):"
  if command -v last &> /dev/null; then
  last -a | head -n 5
  else
  echo "The 'last' command is not available."
  fi

}
