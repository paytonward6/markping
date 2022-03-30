# network-tools

## Overview

This is a hobby project to get more experience with programming in python. If you find this, feel free to let me know your thoughts for future improvements.

### About src/mdping*.py

- Allows one to ping a list of IPs, domain names, DNS servers, etc. and output the results in Markdown format. 
- I personally wanted to be able to use this with [grip -b /path/to/markdown_file.md](https://github.com/joeyespo/grip)

#### mdping vs. mdping_pythonping
- mdping uses the pre-installed *subproccess* package and the ping command pre-installed on the system
    - by using the ***ping*** command, more parameters can be implemented than *pythonping* has (plan on allowing the user to pass these parameters themselves in the future, however as of now **wait** and **count** are just variables in the script).
    - *wait* and *count* can be changed directly in the source with variables **ping_wait_duration** respectively **ping_count**.

- *pythonping* can only be used with **sudo**. mdping's implementation with *subprocess* eliminates the use of sudo.
