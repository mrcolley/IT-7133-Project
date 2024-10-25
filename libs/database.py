import sqlite3
import os
from datetime import datetime

# Initialize the database
def init_db():
    conn = sqlite3.connect('assets/metadata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            audio_path TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save metadata for captured items
def save_metadata(image_path, audio_path):
    conn = sqlite3.connect('assets/metadata.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO metadata (image_path, audio_path, timestamp) 
        VALUES (?, ?, ?)
    ''', (image_path, audio_path, timestamp))
    conn.commit()
    conn.close()

# Example of how to retrieve metadata
def get_metadata():
    conn = sqlite3.connect('assets/metadata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM metadata')
    data = cursor.fetchall()
    conn.close()
    return data

# Call init_db once when the app starts
init_db()
