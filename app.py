from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)
FILE = 'notes.txt'

def load_notes():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def save_notes(notes):
    with open(FILE, 'w', encoding='utf-8') as f:
        for n in notes:
            f.write(n + '\n')

INDEX_HTML = """<!doctype html>
<title>Notes</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body{font-family: system-ui, -apple-system, Roboto, Arial; padding:18px; background:#f8fafc; color:#0f172a;}
  form{margin-bottom:12px;}
  input{name:note; padding:8px; width:60%;}
  button{padding:8px 10px; background:#0b74de; color:white; border:none; border-radius:6px;}
  ul{padding-left:18px;}
  a{color:#0b74de; text-decoration:none; margin-left:8px;}
</style>
<h1>Notes</h1>
<form method="post" action="/add">
  <input name="note" placeholder="Write a note" required>
  <button type="submit">Add</button>
</form>
<ul>
  {% for i,n in enumerate(notes) %}
    <li>{{i+1}}. {{n}} <a href="/delete/{{i}}">Delete</a></li>
  {% endfor %}
</ul>
"""


@app.route('/')
def index():
    notes = load_notes()
    return render_template_string(INDEX_HTML, notes=notes)

@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('note', '').strip()
    if text:
        notes = load_notes()
        notes.append(text)
        save_notes(notes)
    return redirect(url_for('index'))

@app.route('/delete/<int:idx>')
def delete(idx):
    notes = load_notes()
    if 0 <= idx < len(notes):
        notes.pop(idx)
        save_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
