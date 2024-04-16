import git
import os
import datetime

path = os.getcwd()
repo = git.Repo(f"{path}/.git/")

repo.index.commit(f"{datetime.datetime.now()}")

