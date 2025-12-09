import os
import random
import subprocess
from datetime import datetime, timedelta

def git_commit(message, commit_date):
    subprocess.run(['git', 'add', 'info.txt'])
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    subprocess.run(['git', 'commit', '-m', message, '--date', commit_date.strftime('%Y-%m-%dT%H:%M:%S')], env=env)

def git_push():
    subprocess.run(['git', 'push'])

def fake_commits(start_date, end_date, min_commits, max_commits, skipping=False, max_skip_days=1):
    file_path = "info.txt"
    current_date = start_date

    while current_date <= end_date:
        if skipping and random.choice([True, False]):
            skip_days = random.randint(0, max_skip_days)
            print(f"\n\nSkipping {skip_days} days from {current_date.strftime('%d-%b-%Y')}")
            current_date += timedelta(days=skip_days)
            continue

        n_commits = random.randint(min_commits, max_commits)
        print(f"\n\n{n_commits} commits for date: {current_date.strftime('%d-%b-%Y')}")

        for i in range(1, n_commits + 1):
            info = f"Date: {current_date.strftime('%d-%b-%Y')}, Commit #: {i}"     
            with open(file_path, "w") as file:
                file.write(info)
            print(info)
            git_commit(info, current_date)

        current_date += timedelta(days=1)
    
    git_push()

# Merged date configuration
start_date = datetime(2024, 1, 1)   # Start from 01-Jan-2024
end_date = datetime(2025, 12, 9)    # Until present (09-Dec-2025)
min_commits = 1
max_commits = 5

fake_commits(start_date, end_date, min_commits, max_commits, skipping=False, max_skip_days=0)