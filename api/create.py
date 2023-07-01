import requests
import common

common.add_module("scripts")
from repos import get_repos_url_dict

"""
  Create a repository for each repo in the
  repositories URL dictionary.

  The assumption held is that all repos are owned
  by the individual running this script.
"""
def create_repos(access_token, repos_url_dict):
  for repo_name in repos_url_dict:
    print(f"Creating {repo_name}")

    create_url = common.BASE_URL + f"/user/repos/"
    body = create_body(repo_name)

    response = requests.post(
      create_url,
      data=body,
       headers=common.token_header(access_token)
    )

    if (response.status_code == 201):
      print(f"{repo_name} successfully created")
    elif (response.status_code == 409):
      print(f"{repo_name} already exists")
    elif (response.status_code == 422):
      print(f"Validation error")
      print(response.json())
    else:
      print(response)
      print(f"Failed to create repository for {repo_name}")

  return

def create_body(repo_name):
  return {
      "name": repo_name
    }

def main():
  token = common.TOKEN
  if token == "":
    token = common.login()

  create_repos(token, get_repos_url_dict())

if __name__ == "__main__":
  main()