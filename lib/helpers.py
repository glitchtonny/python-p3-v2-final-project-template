# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()


import sqlite3
from models.journal_entry import JournalEntry

DATABASE = "journal.db"

def create_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_id INTEGER,
                name TEXT NOT NULL,
                FOREIGN KEY (entry_id) REFERENCES journal_entries(id) ON DELETE CASCADE
            )
        """)
        conn.commit()

def add_entry(entry):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO journal_entries (title, content, date)
            VALUES (?,?,?)
        """, (entry.title, entry.content, entry.date))
        entry_id = cursor.lastrowid

        for tag in entry.tags:
            cursor.execute("INSERT INTO tags (entry_id, name) VALUES (?, ?)", (entry_id, tag))
        
        conn.commit()
        return entry_id

def get_all_entries():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT journal_entries.id, title, content, date, GROUP_CONCAT(tags.name)
            FROM journal_entries
            LEFT JOIN tags ON journal_entries.id = tags.entry_id
            GROUP BY journal_entries.id
        """)
        rows = cursor.fetchall()
        entries = []
        for row in rows:
            entry_id, title, content, date, tags = row
            tags_list = tags.split(',') if tags else []
            entries.append(JournalEntry(entry_id, title, content, tags_list, date))
        return entries

def find_entries_by_tag(tag):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT journal_entries.id, title, content, date, GROUP_CONCAT(tags.name)
            FROM journal_entries
            LEFT JOIN tags ON journal_entries.id = tags.entry_id
            WHERE tags.name = ?
            GROUP BY journal_entries.id
        """, (tag,))
        rows = cursor.fetchall()
        entries = []
        for row in rows:
            entry_id, title, content, date, tags = row
            tags_list = tags.split(',') if tags else []
            entries.append(JournalEntry(entry_id, title, content, tags_list, date))
        return entries

def delete_entry(entry_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM journal_entries WHERE id=?", (entry_id,))
        conn.commit()

def update_entry(entry_id, title, content, tags, date):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE journal_entries
            SET title=?, content=?, date=?
            WHERE id=?
        """, (title, content, date, entry_id))
        cursor.execute("DELETE FROM tags WHERE entry_id=?", (entry_id,))
        
        for tag in tags:
            cursor.execute("INSERT INTO tags (entry_id, name) VALUES (?, ?)", (entry_id, tag))
        
        conn.commit()




































