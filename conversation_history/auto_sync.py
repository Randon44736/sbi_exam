import subprocess
import os
import sys
import datetime

def run_cmd(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def auto_sync():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    code, root_dir, _ = run_cmd("git rev-parse --show-toplevel", cwd=current_dir)
    repo_dir = root_dir if code == 0 and os.path.isdir(root_dir) else os.path.abspath(os.path.join(current_dir, ".."))

    code, out, _ = run_cmd("git status --porcelain", cwd=repo_dir)
    if not out:
        print("No changes detected. Repository is up to date.")
        return

    print("Detected changes:\n" + out)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"auto-sync: update study progress & records ({timestamp})"

    run_cmd("git add .", cwd=repo_dir)
    code, c_out, c_err = run_cmd(f'git commit -m "{commit_msg}"', cwd=repo_dir)
    if code != 0:
        print("Commit output:", c_out, c_err)
        return

    code, p_out, p_err = run_cmd("git push origin main", cwd=repo_dir)
    if code == 0:
        print("Successfully synced and pushed changes to GitHub.")
    else:
        print("Push error:", p_err)

if __name__ == "__main__":
    auto_sync()
