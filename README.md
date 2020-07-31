# SysExpose

## Why I Did This

As one of my first useful Python Projects, I have created a tool which can be used to monitor system information and related statistics. 

## Features
Currently, it does the following:

### System
- System Information (OS, System Architecture etc.)
- CPU Information (core count, usage etc.)
- Memory Information (currently installed, usage, swap etc.)
- Boot Time (self-explanatory, but system uptime will be in a future update.)
- Disk Information (currently installed, capacities, filesystem etc.)

### Networking

- Network Information (all interfaces, and available IP addresses)
- Private IP (default route, useful when trying to establish SSH access.)
- Public IP (useful to find out if WAN address is static or dynamic)

## Installation 
### Easy Mode:
1. You can easily get setup by using the latest production version in the releases page.
2. Run the following command, where $FILE is the latest wheel from the releases page:
    ```
    pip install $FILE
    ```
3. Create a python file which will contain the following.
    ```
    from SysExpose import Expose
    Expose()
    ```
4. Run the python file you created with -h as the argument. This will display the help dialog.
5. Use the commands in the help dialog to use the functions provided.

### Run from Source

1. If you choose not to use the packaged wheel from the releases page, then you can choose to run the py file alone. 
2. Clone the repository, using git:
    ```
    git clone https://github.com/SurajApps/SysExpose
    ``` 
3. Run the SysExpose.py file and use steps 4-5 from the easy installation above to continue. 

## Bugs and Feature Requests
### Bugs
If you encounter a bug or anything that is not proper practice, please make an issue using the bug template. I will work to fix this when I am next able.

### Feature Requests
If you would like a feature to be implemented within this program, please make an issue using the Feature Request Template. I will aim to work on these after I have completed any pending PLAN and BUG issues. 

