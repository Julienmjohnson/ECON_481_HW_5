#Exercise 0

def github() -> str:
    """
    This returns the link to the github repository for this assignment
    """

    return "https://github.com/Julienmjohnson/ECON_481_HW_5/blob/main/HW5.py"

#Exercise 1
import requests
from bs4 import BeautifulSoup
import re

def scrape_code(url: str) -> str:
    """
    This takes url of the course website lecture as a string and returns all of the python code that was within that lecture.
    """
    req_obj = requests.get(url)

    soup = BeautifulSoup(req_obj.text)
    pythonCodeChunks = soup.find_all("code", attrs={"class": "sourceCode python"})
    codeChunks = []
    for x in pythonCodeChunks:
        codeChunks.extend(x.find_all("span", attrs={"id": re.compile('cb\d+-\d')}))

    codetext = ""
    for x in codeChunks:
        if len(x.text) > 0:
            if not (x.text[0] == "%"):
                codetext += x.text
                codetext += " "
    if len(codetext) > 0:
        codetext = codetext[:-1]

    return codetext