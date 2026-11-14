import time
import os
import sys
import datetime

# Add current dir to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sync_core import perform_git_sync, run_cmd, BRAIN_DIR, REPO_DIR

LOG_FILE = os.path.join(REPO_DIR, "conversation_history", "sync_daemon.log")

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass

def get_transcript_state():
    t_path = os.path.join(BRAIN_DIR, ".system_generated", "logs", "transcript.jsonl")
    if os.path.exists(t_path):
        return (os.path.getmtime(t_path), os.path.getsize(t_path))
    return (0, 0)

def main():
    log("Auto-sync daemon started. Monitoring repository and conversation transcripts...")
    last_transcript_state = (0, 0)

    while True:
        try:
            current_state = get_transcript_state()
            code, git_status, _ = run_cmd("git status --porcelain")

            # Check if transcript updated or git files changed
            transcript_changed = (current_state != last_transcript_state and current_state != (0, 0))
            git_changed = bool(git_status.strip())

            if transcript_changed or git_changed:
                log(f"Change detected (TranscriptChanged={transcript_changed}, GitChanged={git_changed}). Performing sync...")
                success, msg = perform_git_sync()
                log(f"Sync result: {msg}")
                last_transcript_state = current_state
            
        except Exception as e:
            log(f"Daemon exception: {e}")

        time.sleep(15)

if __name__ == "__main__":
    main()
