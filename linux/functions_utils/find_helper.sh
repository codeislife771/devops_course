find_helper () {
  read -p "Choose search method:
  1) By Name
  2) By Size
  3) By Modification Time
  4) By Permissions
  Q) Quit
  Enter your choice: " choice

  case "$choice" in
    1) # Search by Name
      read -p "Enter name to search for: " name
      read -p "Enter path to search in (default: '.'): " path
      path="${path:-.}" # Use current directory if path is empty
      printf "\nSearching for files named '%s' in '%s'...\n\n" "$name" "$path"
      find "$path" -type f -name "$name"
      ;;
    2) # Search by Size
      read -p "Enter size criteria (e.g., +1M, -500k, 10G): " size_criteria
      read -p "Enter path to search in (default: '.'): " path
      path="${path:-.}"
      printf "\nSearching for files with size '%s' in '%s'...\n\n" "$size_criteria" "$path"
      find "$path" -type f -size "$size_criteria"
      ;;
    3) # Search by Modification Time
      read -p "Enter modification time criteria (e.g., -mtime -7 for files modified in the last 7 days): " mtime_criteria
      read -p "Enter path to search in (default: '.'): " path
      path="${path:-.}"
      printf "\nSearching for files modified '%s' in '%s'...\n\n" "$mtime_criteria" "$path"
      find "$path" -type f -mtime "$mtime_criteria"
      ;;
    4) # Search by Permissions
      read -p "Enter permission criteria (e.g., -perm 755): " perm_criteria
      read -p "Enter path to search in (default: '.'): " path
      path="${path:-.}"
      printf "\nSearching for files with permissions '%s' in '%s'...\n\n" "$perm_criteria" "$path"
      find "$path" -type f -perm "$perm_criteria"
      ;;
    Q|q) # Quit
      echo "Exiting find helper."
      return 0
      ;;
    *)
      echo "Invalid choice. Please select a valid option."
      ;;
  esac
}

