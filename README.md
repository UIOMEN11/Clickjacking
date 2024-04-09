# Clickjacking

This Python script checks for Clickjacking vulnerability on a given domain by analyzing the presence of specific HTTP headers.

Usage
Ensure you have Python installed on your system.
Install the requests library using pip:
Copy code
pip install requests
Modify the domain variable in the script to the URL you want to test.
Run the script:
Copy code
python clickjacking_checker.py
Script Details
The script uses the requests library to send a GET request to the specified domain.
It checks for the presence of the X-Frame-Options and Content-Security-Policy headers in the response.
If both headers are present, the script concludes that the domain is not vulnerable to Clickjacking.
If either of the headers is missing, the script indicates that the domain is vulnerable to Clickjacking and specifies which headers are missing.
