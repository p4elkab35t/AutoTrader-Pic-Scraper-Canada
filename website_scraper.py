import requests
import re

def get_plain(URL="https://www.google.com"):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'}
    response = requests.get(URL, headers=headers)
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
