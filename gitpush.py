#!/usr/bin/env python


import subprocess
import sys

def git_push(commit_message, remote_link):
    # Initialize a Git repository
    subprocess.run(['git', 'init'])

    # Add all files to staging area
    subprocess.run(['git', 'add', '.'])

    # Commit changes
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Add a remote repository
    subprocess.run(['git', 'remote', 'add', 'origin', remote_link])

    # Push changes to the remote repository
    subprocess.run(['git', 'push', '-u', '-f', 'origin', 'main'])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: gitpush 'commit message' 'remote link'")
        sys.exit(1)

    commit_message = sys.argv[1]
    remote_link = sys.argv[2]

    git_push(commit_message, remote_link)