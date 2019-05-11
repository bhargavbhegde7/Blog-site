#from git import Repo
#import subprocess

'''
print("getting the repo etc")

repo_dir = '/home/pi/bhargavbhegde7.github.io'
repo = Repo(repo_dir)
file_list = ['utils.html']
commit_message = 'Change ip address of pi'
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
#subprocess.call(["cd", "/home/pi/bhargavbhegde7.github.io/"], shell=True)
#subprocess.call(["ls", "-ltrh"], shell=True)
#subprocess.call(["df", "-h"])

subprocess.call(["git config credential.helper store"], shell=True)
subprocess.call(["git status"], shell=True)
subprocess.call(["git add utils.html"], shell=True)
#subprocess.call(["git add ."], shell=True)
subprocess.call(["git status"], shell=True)
subprocess.call(["git commit -m \"tunnel url change\" "], shell=True)
subprocess.call(["git push origin master"], shell=True)

