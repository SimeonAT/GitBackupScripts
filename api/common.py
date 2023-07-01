from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()

USERNAME = os.environ["GITEA_USERNAME"]
PASSWORD = os.environ["GITEA_PASSWORD"]
BASE_URL = os.environ["GITEA_BASE_URL"]
TOKEN = os.environ["GITEA_ACCESS_TOKEN"]

"""
  Wrapper function for adding an outside module.

   https://pythonhow.com/what/what-to-do-to-import-files-from-different-folder-in-python/
"""
def add_module(module_name):
  module_path = os.path.abspath(module_name)
  sys.path.append(module_path)
  return

"""
  Logs in as a specified user into
  the Gitea server.
"""
def login():
    login_url = BASE_URL + f"/users/{USERNAME}/tokens"
    response = requests.get(login_url, auth=(USERNAME, PASSWORD))
    body_array = response.json()[0]

    return extract_token(body_array)

"""
  Extract access token from the HTTP login response.
  Raise error if no access token is found.
"""
def extract_token(body):
  if (body == []):
    print(
       "The user has no access tokens. " +
       "Please generate a new one."
      )
  elif (body["sha1"] == ""):
    print(
       "Access token not found. " +
       "Please generate a new one."
      )

  print("Login successful!")
  return body["sha1"]

def token_header(access_token):
  return {"Authorization": f"token {access_token}"}