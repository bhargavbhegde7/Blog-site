'''
from git import Repo

print("getting the repo etc")

repo_dir = '/home/pi/bhargavbhegde7.github.io'
repo = Repo(repo_dir)
file_list = ['utils.html']
commit_message = 'Change the tunnel url'
repo.index.add(file_list)
print("files added")
repo.index.commit(commit_message)
print("committed")
origin = repo.remote('origin')
origin.push()

print("pushed")

print("done deal!!")
'''


import subprocess
import os
os.chdir("/home/pi/bhargavbhegde7.github.io/")
subprocess.call(["sudo git config credential.helper store"], shell=True)
subprocess.call(["sudo git add ."], shell=True)
print("added")
subprocess.call(["sudo git commit -m \"tunnel url change\" "], shell=True)
print("committed")
subprocess.call(["sudo git push origin master"], shell=True)
print("pushed")
