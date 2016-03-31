# Ethbot 1.1


An mailbot for Ethereum https://www.ethereum.org/ that sends you daily mails or threshold mails written in Python.

Currently only working with Gmail's smtp, for future support.
You may have to change Gmails security settings according to raised errors.

1. http://www.google.com/accounts/DisplayUnlockCaptcha
2. https://support.google.com/accounts/answer/6010255

for usage call the script with int arguments.

"python ethbot.py 12" will wait until ETH reaches 12$ and sends you an mail if so.

Added wallet balance access through an API.
