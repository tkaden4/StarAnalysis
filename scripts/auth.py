import os
from argparse import ArgumentParser

def get_auth():
    raise NotImplementedError()

def get_user_auth():
    return {"login_or_token": os.environ["USER"], "password": os.environ["PASSWORD"]}

def get_oauth2_auth():
    raise NotImplementedError()
