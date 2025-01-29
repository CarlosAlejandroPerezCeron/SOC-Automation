import sqlite3

def init_db():
    conn = sqlite3.connect("soc_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            event_type TEXT,
            details TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_log(event_type, details):
    conn = sqlite3.connect("soc_logs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (event_type, details) VALUES (?, ?)", (event_type, details))
    conn.commit()
    conn.close()
