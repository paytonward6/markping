# markping (Markdown Ping)

## Overview

This is a hobby project to get more experience with programming in python. If you find this, feel free to let me know your thoughts for future improvements.

### About src/markping*.py

- Allows one to ping a list of IPs, domain names, DNS servers, etc. and output the results in Markdown format. 
- I personally wanted to be able to use this with [grip](https://github.com/joeyespo/grip)
like this 
```console
   $ grip -b /path/to/markdown/file.md
```

#### markping vs. markping_pythonping
- markping uses the pre-installed *subproccess* package and the ping command pre-installed on the system
    - by using the ***ping*** command, more parameters can be implemented than [pythonping](https://github.com/alessandromaggio/pythonping) has (plan on allowing the user to pass these parameters themselves in the future, however as of now **wait** and **count** are just variables in the script).
    - *wait* and *count* can be changed directly in the source with variables **ping_wait_duration** respectively **ping_count**.

- *pythonping* can only be used with **sudo**. markping's implementation with *subprocess* eliminates the use of sudo.

### Requirements
- tqdm (4.63.1)
- pythonping (1.1.1)
    - only if using markping_pythonping.py
#### Note
- The only other version of *tqdm* I have used with markping.py is 4.62.3, so please let me know if it does not work with your version.

### Installation
```console
    $ git clone https://github.com/paytonward6/markping.git
```

### Usage
```console
    $ python3 markping.py <ping list>.txt <ping results>.md
```
