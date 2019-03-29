import pandas as pd
import wikipedia as wk
import os.path as path
from urllib.parse import urlparse, unquote, quote

# Read in frame with columns "language" and "url"
df = pd.read_csv("data/language_links.csv")

# Get the page title (unencoded) from the url
def page_title(url):
    urlpath = urlparse(url).path
    _, title = path.split(urlpath)
    return unquote(title)

# Add the page title to the dataset
df["title"] = df["url"].map(page_title)

df.to_csv("data/languages.csv", index=False)
