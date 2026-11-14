import subprocess
import os
import sys
import datetime

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def auto_sync():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_dir)

    # Check git status
    code, out, _ = run_cmd("git status --porcelain")
    if not out:
        print("No changes detected. Repository is up to date.")
        return

    print("Detected changes:\n" + out)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"auto-sync: update study materials and progress ({timestamp})"

    run_cmd("git add .")
    code, c_out, c_err = run_cmd(f'git commit -m "{commit_msg}"')
    if code != 0:
        print("Commit output:", c_out, c_err)
        return

    code, p_out, p_err = run_cmd("git push origin main")
    if code == 0:
        print("Successfully synced and pushed changes to GitHub.")
    else:
        print("Push error:", p_err)

if __name__ == "__main__":
    auto_sync()
