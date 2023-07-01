from git import Repo
import os

from repos import get_repos_url_dict
from common import *

"""
  Clones all repositories referenced in the
  dictionary containing Git URLs.
"""
def clone(repos_dict):
    repos = {}

    for repoName in repos_dict.keys():
        print(f"Cloning {repoName}")

        url = repos_dict[repoName]
        path = os.path.join(BACKUP_DIR, repoName)

        repos[repoName] = Repo.clone_from(url, path)
        ssh_init(repos[repoName])

        print(f"Finished {repoName}")

    return repos

"""
  Does "git pull" on all repos in "/backups"
  to ensure they are up to date.
"""
def pull(repos):
    for name in repos.keys():
        repo = repos[name]
        repo.git.pull()

        print(f"{name} successfully pulled")
    return

def no_backups():
    if "backups" not in os.listdir():
        return True
    else:
        return False

def main():
  repos_dict = {}

  if no_backups():
      repos_dict = clone(get_repos_url_dict())
  else:
      repos_dict = attach(BACKUP_DIR, ssh=True)
      pull(repos_dict)

if __name__ == "__main__":
  main()