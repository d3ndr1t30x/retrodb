from flask import Flask, render_template, request, send_file, redirect, url_for
import csv
import os
import random
from pygments import highlight
from pygments.lexers import PythonLexer, CLexer, CppLexer, PhpLexer, RubyLexer, PerlLexer, JavaLexer, guess_lexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

def load_exploits():
    csv_path = 'exploitdb/files_exploits.csv'
    exploits = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            exploits.append({
                'date': row['date_published'],
                'description': row['description'],
                'platform': row['platform'],
                'type': row['type'],
                'file': row['file']
            })
    exploits.sort(key=lambda x: x['date'], reverse=True)
    return exploits

def get_unique_values(exploits, key):
    values = set()
    for e in exploits:
        val = e[key]
        if val:
            values.add(val)
    return sorted(values)

def apply_filters(exploits, q=None, platform=None, type_=None):
    filtered = exploits
    if q:
        filtered = [e for e in filtered if q.lower() in e['description'].lower()]
    if platform:
        filtered = [e for e in filtered if e['platform'].lower() == platform.lower()]
    if type_:
        filtered = [e for e in filtered if e['type'].lower() == type_.lower()]
    return filtered

exploits = load_exploits()
unique_platforms = get_unique_values(exploits, 'platform')
unique_types = get_unique_values(exploits, 'type')

@app.route('/')
def index():
    q = request.args.get('q', '').strip()
    platform = request.args.get('platform', '').strip()
    type_ = request.args.get('type', '').strip()
    
    # If q is cleared (empty), clear all filters
    if q == '':
        platform = ''
        type_ = ''
    
    has_filters = q or platform or type_
    if has_filters:
        display_exploits = apply_filters(exploits, q, platform, type_)
    else:
        display_exploits = exploits[:50]
    
    return render_template('index.html', 
                           exploits=display_exploits, 
                           q=q, 
                           platform=platform, 
                           type_=type_,
                           unique_platforms=unique_platforms,
                           unique_types=unique_types)

@app.route('/exploit')
def exploit():
    path = request.args.get('path')
    if not path:
        return "No path specified", 400
    full_path = os.path.join('exploitdb', path)
    if not os.path.exists(full_path):
        return "File not found", 404
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Syntax highlighting
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == '.py':
            lexer = PythonLexer()
        elif ext in ['.c', '.h']:
            lexer = CLexer()
        elif ext in ['.cpp', '.cc', '.cxx', '.hpp']:
            lexer = CppLexer()
        elif ext == '.php':
            lexer = PhpLexer()
        elif ext == '.rb':
            lexer = RubyLexer()
        elif ext == '.pl':
            lexer = PerlLexer()
        elif ext == '.java':
            lexer = JavaLexer()
        else:
            lexer = guess_lexer(content)
        formatter = HtmlFormatter(style='monokai', noclasses=True)
        highlighted_content = highlight(content, lexer, formatter)
    except:
        highlighted_content = content  # fallback to plain text
    
    return render_template('exploit.html', content=highlighted_content, path=path)

@app.route('/download')
def download():
    path = request.args.get('path')
    if not path:
        return "No path specified", 400
    full_path = os.path.join('exploitdb', path)
    if not os.path.exists(full_path):
        return "File not found", 404
    return send_file(full_path, as_attachment=True)

@app.route('/random')
def random_exploit():
    if not exploits:
        return "No exploits available", 404
    random_e = random.choice(exploits)
    return redirect(url_for('exploit', path=random_e['file']))

if __name__ == '__main__':
    app.run(debug=True)