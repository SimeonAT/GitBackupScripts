from backup import *
from repos import get_repos_url_dict
from common import *

"""
  Upload local Git repos to Gitea server,
  by using the Git URLS provided in in the Repos Dictionary.
"""
def upload(repos_url_dict):
    repos_dict = attach(BACKUP_DIR)

    for repoName in repos_dict.keys():
        repo = repos_dict[repoName]
        repoURL = repos_url_dict[repoName]

        print(f"Uploading {repoName} to Gitea")

        try:
          repo.git.remote("rm", "origin")
        except:
          print("No remote origin to remove")

        repo.git.remote("add", "origin", repoURL)
        repo.git.push("-u", "origin", "main")

        print(f"{repoName} has been successfully uploaded to Gitea")

    return

def main():
   upload(get_repos_url_dict())

if __name__ == "__main__":
  main()