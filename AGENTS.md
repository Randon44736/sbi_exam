# Workspace Rules: Automatic Git Sync

## 1. Silent Automatic Git Push on Any Update
Whenever you (the AI assistant) make or find any change in this folder (e.g., creating/updating chapter notes, updating study progress, exporting chat history, or adding files):
- **ALWAYS** automatically stage, commit, and push the changes to GitHub (`origin main`):
  ```powershell
  git add .
  git commit -m "<concise descriptive summary of changes>"
  git push origin main
  ```
- **Do this automatically in the background** without waiting for or asking user confirmation.

## 2. Conversation & Progress State Preservation
- Keep `STUDY_PROGRESS_STATUS.md` and the relevant chapter notes (`ch *.txt`) updated as Hitendra completes questions and chapters.
- Whenever new lessons are completed, append the update to `CHAT_HISTORY_IBPS_RRB_PO_QUANT.md` and push to git so no progress is ever lost across laptop changes.
