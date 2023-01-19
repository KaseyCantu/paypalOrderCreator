## Automated Selenium PayPal Order Generator

This script runs on `Python 3` - if you do not already have it installed you can get it for [MacOS](https://www.python.org/downloads/macos/) or [Windows](https://www.python.org/downloads/windows/). You can verify which version you are currently running by using `python3 --version`.
 
Alternatively, if you use `asdf` you can run `asdf install python 3.11.1` to get more easily download the latest stable version of `Python 3`.

- Start by installing selenium, it is the only dependency for this script: 
```bash
pip3 install selenium 
```

- Run the script: 
```bash
python3 main.py
```
- You will be met with prompts that ask for your Sandbox Paypal Account username and password to be used for login. This will need to be the account you wish to send money from. 
- Next you will be asked for the recipient PayPal account you wish to send money to.
- Finally, you will be asked how many orders you would like to generate.

> ATTN: :warning: Some websites do not run properly when running `headless` in Chrome. As a result, this script currently does not run headless. Coming soon will be an additional prompt when running the script that asks if you want to run `headless` and have `FireFox` installed to be able to do so.