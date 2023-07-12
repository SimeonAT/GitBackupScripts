# Git Backup Scripts

## Introduction

This repository contains my Python scripts for backing up
and restoring the Git repositories hosted on my self-hosted Gitea server.

These scripts can be used to back up repositories in any self-hosted
Gitea server.

## Instructions

### Setup

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

3. Run `make install` to install the dependencies.

### Usage

#### Backing up

1. Run `make backup` to backup the Gitea repositiories associated
   with user identified by `GITEA_USERNAME`, as set in `.env`.
   Depending on how large the repositories are, the script may
   take quite some time to complete. When the script is finished,
   it will output a `/backup` directory in the root directory
   of this repository.

#### Restoring

These steps assume that the repositories to be backed up are in the
created `/backup` directory.

1. Run `make create` to create empty Gitea repositories, corresponding
   to the name of each repository in `/backup`.

2. Run `make restore` to upload the local Git repositories in `/backup`
   to their associated empty repositories (which we created in `make create`).
   Depending on how large the repositories are, the script may
   take quite some time to complete.

#### Deleting

In addition, there is a provided `make delete` function to delete
the repositories, held locally in `/backup`, from the Gitea server.

I made this script to delete unaccessible repositories (that I already backed up in `/backup`), before following steps laid out in the above **Restoring** section (in order to restore accessible versions of said repositories).

### Testing

The scripts can take quite a long time to run, which could
delay the detection of a possible prolem until late in the backup process.
Furhtermore, it could be the case that the values set in `.env` are outdated or do not currently work.

To detect these issues, there is a [test version](https://github.com/SimeonAT/GitBackupScripts/blob/main/scripts/repos.py#L27) of the repositories dictionary in `/script/repos.py`.

That way, you can:

1. Place a few small sized repositories,

2. Set the [testing flag](eonAT/GitBackupScripts/blob/main/scripts/repos.py#L5) to true, and

3. Run steps defined in **Usage** to determine if you are able to back-up and restore successfully,

before doing any actual backups.