import requests
import common

common.add_module("scripts")
from repos import get_repos_url_dict

"""
  Deletes all repositories that have mappings in
  "REPO_URL_DICT".

  The assumption held is that all repos are owned
  by the individual running this script.
"""
def delete_repos(access_token, repos_url_dict):
  for repo_name in repos_url_dict:
    delete_url = \
      f"{common.BASE_URL}/repos/{common.USERNAME}/{repo_name}"

    response = requests.delete(
       delete_url,
       headers=common.token_header(access_token)
      )

    if (response.status_code == 204):
      print(f"{repo_name} successfully deleted")
    elif (response.status_code == 404):
      print(f"{repo_name} does not exist")    
    elif (response.status_code == 403):
      print(f"You are not authorized to delete {repo_name}")
    else:
      print(f"Failed to delete {repo_name}")

  return

def main():
  token = common.TOKEN
  if token == "":
    token = common.login()

  delete_repos(token, get_repos_url_dict())

if __name__ == "__main__":
  main()