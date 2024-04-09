import requests

domain = "https://www.rknec.edu/"
response = requests.get(domain)
headers = response.headers
# Print all existing headers
print("Existing Headers:")
for header, value in headers.items():
    print(f"{header}: {value}")

# Check for X-Frame-Options and Content-Security-Policy headers
if 'X-Frame-Options' in headers and 'Content-Security-Policy' in headers:
    print("\n" + domain + " is not vulnerable to CLICKJACKING")
else:
    print("\n" + domain + " is vulnerable to CLICKJACKING")
    if 'X-Frame-Options' not in headers:
        print("Missing Header: X-Frame-Options")
    if 'Content-Security-Policy' not in headers:
        print("Missing Header: Content-Security-Policy")
