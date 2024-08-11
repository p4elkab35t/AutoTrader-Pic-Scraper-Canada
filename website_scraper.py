import requests
import re

def get_plain(URL="https://www.google.com"):
    response = requests.get(URL)
    html_content = response.text
    return html_content

def get_images(plainHTML):
    regex = r'"image":\s*\[\s*("https?://[^"]+"\s*(,\s*"https?://[^"]+")*)\s*\]'
    matches = re.search(regex, plainHTML, re.MULTILINE)
    if matches:
        links_string = matches.group(1)
        links = [link.strip().strip('"') for link in links_string.split(',')]
        return links
    else:
        return []
