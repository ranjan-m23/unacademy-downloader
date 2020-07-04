# Downloader for Unacademy.
This script downloads lecture slides for individual lectures of a course of Unacademy.

### Usage
1. Clone this repo to a python environment (preferably a virtual one).
2. install file dependencies:```python pip install -r requirements.txt```
3. Run ``` download.py```:
```python3 download.py```

4. The script will ask for 3 inputs:
    * Login number: The phone to which a login otp will be sent.
    * OTP: the otp recieved by the phone so that the script can login.
    * course url : this the url of an unacademy course , will be of the format: ```https://unacademy.com/course/*```.
    Provide these inputs accordingly.

_________