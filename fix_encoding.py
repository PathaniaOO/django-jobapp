from pathlib import Path

p = Path('sqlite_data.json')
raw = p.read_bytes()
try:
    raw.decode('utf-8')
    print("sqlite_data.json is valid UTF-8.")
except UnicodeDecodeError:
    print("Re-encoding from cp1252 to UTF-8...")
    txt = raw.decode('cp1252')
    p.write_text(txt, encoding='utf-8')
    print("Rewritten as UTF-8.")
