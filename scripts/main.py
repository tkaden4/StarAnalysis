from stars import *
from auth import *
from multiprocessing import Pool
import os
import sys
import json

def repo_json(repo):
    return json.dumps({
        "language": repo.language,
        "name": repo.name,
        "open_issues": repo.open_issues,
        "stargazers": repo.stargazers_count,
        "topics": repo.topics,
        "url": repo.url,
        "description": repo.description,
        "fork": repo.fork,
        "forks_count": repo.forks_count,
        "created_at": repo.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "watchers_count": repo.watchers_count})

if __name__ == "__main__":
    user = os.environ["USER"]
    auth = get_user_auth()
    try:
        with Pool(4) as p:
            for star in p.imap_unordered(repo_json, get_stars(user, **auth)):
                print(star)
    except KeyboardInterrupt:
        pass
