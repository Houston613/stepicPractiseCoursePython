import urllib.request
import re

import requests

a = input()
b = input()


def checker(url):
    res = requests.get(url)
    if res.status_code == 200:
        try:
            file = urllib.request.urlopen(url)
            readied_Text = file.read()
            readied_string = readied_Text.decode("utf8")
            file.close()
            links = re.findall(r'<a.*href="([^"]*)"', readied_string)
        except:
            return []
        else:
            return links
    else:
        return []


def steps():
    our_links = checker(a)
    for link in our_links:
        another_links = checker(link)
        if b in another_links:
            return True
    return False


if steps():
    print("Yes")
else:
    print("No")
