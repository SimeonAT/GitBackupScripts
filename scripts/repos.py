"""
  Flag to determine whether or not to use the
  test version of the repositories dictionary.
"""
TESTING = True

def get_repos_url_dict():
    if (TESTING):
        return REPO_TEST_DICT
    else:
        return REPO_URL_DICT

"""
  Contains all Gitea repositories to back up.

  Mappings are between the repository name and its
  corresponding Git URL.
"""
REPO_URL_DICT = {
    "Insert repository name": "Insert ssh key",
}

"""
  A version of the dictionary that is used
  for testing purposes.
"""
REPO_TEST_DICT = {
  "Insert repository name": "Insert ssh key",
}