helper() {
    printf "
Welcome to mytoolz - A collection of useful system utilities.

Usage: mytoolz [flag] 

Available flags:

-f: Find Helper - Quickly locate files and directories.
    Includes:
      - Asks you how you want to search (by name, size, etc.).
      - Shows you the files or folders it finds.
    Example:
      mytoolz -f
-s: System Information - Display details about your system.
    Includes:
      - How long the computer has been running.
      - How much memory is free.
      - How full your hard drives are.
      - How many programs are running.
      - Details about your computer's brain (CPU).
    Example:
      mytoolz -s
 -u: User Management - Shows you who is using the computer and the users on it.
    Includes:
      - Who is currently logged in.
      - The total number of users.
      - Users created recently.
      - The types of command lines users prefer.
      - The last few times people logged in.
    Example:
      mytoolz -u

"


}
