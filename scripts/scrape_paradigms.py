from bs4 import BeautifulSoup as BSoup

def find_paradigms(page):
    soup = BSoup(page, "html.parser")
    # Find the infobox and work way to the elements of the table
    paradigm_a = soup.find("a", attrs={"title": "Programming paradigm"})
    if paradigm_a == None:
        return None
    paradigm_th = paradigm_a.parent
    paradigm_td = paradigm_th.next_sibling
    # Extract the names from the <a> elements in the infobox
    paradigms = [child.string.lower() for child in paradigm_td.children if child.name == 'a']
    return paradigms


import pandas as pd
import requests as req

df = pd.read_csv("data/languages.csv")

def map_row(row):
    try:
        # We get errors if the file doesnt have 
        return find_paradigms(req.get(row).text)
    except:
        return None

# This computation takes a while
print("Getting lists of paradigms from wikipedia, may take a while...")
df["paradigms"] = df["url"].map(map_row)

# Write the new data to file
print("Finished.")
df.to_csv("data/languages_para.csv", index=False)
