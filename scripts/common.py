from git import Repo 
from dotenv import load_dotenv
import os

load_dotenv()

BACKUP_DIR = os.path.join(os.curdir, "backups")

"""
  Create a Python reference for each repository
  in the backups directory.
"""
def attach(backup_dir, ssh=False):
    repos = {}

    for repoName in os.listdir(backup_dir):
        repo_path = os.path.join(backup_dir, repoName)

        repos[repoName] = Repo.init(repo_path)
        if (ssh):
          ssh_init(repos[repoName])

        print(f"{repoName} successfully found")

    return repos

"""
  Tells GitPython to use the SSH key set
  in your ".env" file.

  https://gitpython.readthedocs.io/en/3.1.31/tutorial.html?highlight=ssh#handling-remotes
"""
def ssh_init(repo):
  ssh_cmd = f'ssh -i {os.environ["SSH_KEY_PATH"]}'
  with repo.git.custom_environment(GIT_SSH_COMMAND=ssh_cmd):
      repo.remotes.origin.fetch()