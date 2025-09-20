# Notes App (Flask) — Simple deployable example

This is a minimal Flask notes app that stores notes in a local `notes.txt` file.
It's meant for learning and small demos. For production use a proper database.

## Files
- `app.py` — The Flask application.
- `requirements.txt` — Python packages.
- `Procfile` — Start command for many PaaS (gunicorn app:app).
- `.gitignore` — (created below)

## Run locally
1. Create virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run:
   ```
   python app.py
   # or: gunicorn app:app
   ```
4. Open: http://127.0.0.1:5000

## Deploy to Railway (quick)
1. Push this repo to GitHub.
2. In Railway, create a new project and choose "Deploy from GitHub".
3. Select this repo, set start command to `gunicorn app:app` if needed.
4. Railway will build and give you a public URL.

## Notes
- This app stores notes in `notes.txt` in the app folder. On many PaaS, the filesystem is ephemeral — use a database or external storage for persistence.
- Feel free to adapt this code for SQLite/Postgres as a next step.
