import json
import os
import shutil
import re
import subprocess
import datetime

BRAIN_DIR = r"C:\Users\Lenovo\.gemini\antigravity\brain\4da75438-c628-4079-844c-2f2e07743d30"
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd or REPO_DIR)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def sync_chat_transcript():
    raw_transcript = os.path.join(BRAIN_DIR, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(raw_transcript):
        return False, "No transcript file found."

    raw_logs_dir = os.path.join(REPO_DIR, "conversation_history", "raw_logs")
    os.makedirs(raw_logs_dir, exist_ok=True)
    target_transcript = os.path.join(raw_logs_dir, "transcript.jsonl")

    # Check if modified
    if os.path.exists(target_transcript):
        if os.path.getmtime(raw_transcript) == os.path.getmtime(target_transcript) and \
           os.path.getsize(raw_transcript) == os.path.getsize(target_transcript):
            pass # We still process if git changes exist

    shutil.copy2(raw_transcript, target_transcript)

    user_uploaded_dir = os.path.join(BRAIN_DIR, ".user_uploaded")
    if os.path.exists(user_uploaded_dir):
        media_backup = os.path.join(raw_logs_dir, "media")
        os.makedirs(media_backup, exist_ok=True)
        for f in os.listdir(user_uploaded_dir):
            shutil.copy2(os.path.join(user_uploaded_dir, f), os.path.join(media_backup, f))

    with open(raw_transcript, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    chat_md = []
    chat_md.append("# Conversation History: IBPS RRB PO Quantitative Aptitude Lessons\n")
    chat_md.append("**Original Conversation ID:** `4da75438-c628-4079-844c-2f2e07743d30`\\\n")
    chat_md.append("**Subject:** IBPS RRB PO / SBI Exam — Quantitative Aptitude Mentorship & Step-by-Step Problem Solving\\\n")
    chat_md.append("**Candidate:** Hitendrasinh Solanki\\\n")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_md.append(f"**Last Synchronized:** {now_str}\\\n")
    chat_md.append(f"**Total Turns/Steps Recorded:** {len(records)}\n\n---\n")

    for i, r in enumerate(records):
        t = r.get("type")
        created_at = r.get("created_at", "")
        content = r.get("content", "")

        if t == "USER_INPUT":
            clean_content = content
            m = re.search(r"<USER_REQUEST>(.*?)</USER_REQUEST>", content, re.DOTALL)
            if m:
                clean_content = m.group(1).strip()
            chat_md.append(f"### 👤 Hitendra (User) — Step {i:02d} ({created_at})\n\n{clean_content}\n\n---\n")
        elif t == "PLANNER_RESPONSE":
            if content.strip():
                chat_md.append(f"### 🤖 AI Mentor — Step {i:02d} ({created_at})\n\n{content.strip()}\n\n---\n")

    chat_file = os.path.join(REPO_DIR, "conversation_history", "CHAT_HISTORY_IBPS_RRB_PO_QUANT.md")
    with open(chat_file, "w", encoding="utf-8") as f:
        f.write("\n".join(chat_md))

    return True, f"Transcript synchronized ({len(records)} steps)."

def perform_git_sync(custom_msg=None):
    sync_chat_transcript()

    code, out, _ = run_cmd("git status --porcelain")
    if not out.strip():
        return False, "No changes to commit. Everything is up to date."

    print("Detected Git changes:\n" + out)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = custom_msg or f"auto-sync: update study progress, chapter notes & chats ({timestamp})"

    run_cmd("git add .")
    code, c_out, c_err = run_cmd(f'git commit -m "{commit_msg}"')
    if code != 0:
        return False, f"Commit error: {c_out} {c_err}"

    code, p_out, p_err = run_cmd("git push origin main")
    if code == 0:
        return True, "Successfully committed and pushed to GitHub."
    else:
        return False, f"Push error: {p_err}"

if __name__ == "__main__":
    success, msg = perform_git_sync()
    print(msg)
