# Git Backup Scripts

## Introduction

This repository contains my Python scripts for backing up
and restoring data on my self-hosted Gitea server.

These scripts can be used to back up repositories in any self-hosted
Gitea server.

## Instructions

### Usage

1. Navigate to `/scripts/repos.py` to place mappings of your Gitea repository name with their SSH URLs in the `REPO_URL_DICT` dictionary.

2. In the root directory, create a `.env` file and add in the following:
   ```
   GITEA_USERNAME="[insert username here]"
   GITEA_PASSWORD="[insert password here]"
   GITEA_BASE_URL="[inert URL here]"
   GITEA_ACCESS_TOKEN="[insert access token here]"
   ```
   The `GITEA_USERNAME` and `GITEA_PASSWORD` corresponds to the username and password, respectively, of the Gitea account you use in your self-hosted Gitea server.
   The `GITEA_BASE_URL` is the URL of the homepage for your self-hosted
   Gitea server.
   The `GITEA_ACCESS_TOKEN` will contain your Gitea API token. You can find more information on how to obtain the API token in the [Gitea API Documentation](https://docs.gitea.com/development/api-usage#generating-and-listing-api-tokens).

