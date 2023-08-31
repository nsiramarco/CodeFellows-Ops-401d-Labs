
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: Copy the DEMO.md file from class repo > class-38 > challenges and complete the TODOs.
#               Fully annotate any missing comments and populate any missing variables/code
#               Test the script in Web Security Dojo to confirm the output is correct
#               This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame
#               This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php

# Date: 08/30/2023
# Modified by: Natasha Siramarco

### Install requests bs4 before executing this in Python3
# on the Linux vm terminal: 
#                   pip3 install requests
#                   pip3 install beautifulsoup4


# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# Retrieve all forms from URL
def get_all_forms(url):
    # Beautiful soup to parse HTML and find all form tags and vulnerable to XSS attacks
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Extract details from HTM form
def get_form_details(form):
    # Analyze attributs and collect form data
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Submit with input values 
def submit_form(form_details, url, value):
    # Target url to create javascript data payload and see is changes in response content
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# XSS scan on url
def scan_xss(url):
    # Idenify all forms on the url and outputs the findings
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerable")</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

# User input for a URL target to text XSS and scans 
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
# Positive
#       Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
#       [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
#       [+] XSS Detected on https://xss-game.appspot.com/level1/frame
#       [*] Form details:
#       {'action': '',
#        'inputs': [{'name': 'query',
#                    'type': 'text',
#                    'value': '<script>alert("XSS Vulnerable")</script>'},
#                   {'name': None, 'type': 'submit'}],
#        'method': 'get'}
#       True
#       
# Negative
#       Enter a URL to test for XSS:http://dvwa.local/login.php
#       [+] Detected 1 forms on http://dvwa.local/login.php.
#       False
#       