
class JournalEntry:
    def __init__(self, id, title, content, tags, date):
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags
        self.date = date

    def __repr__(self):
        return f"<JournalEntry(id={self.id}, title={self.title}, date={self.date}, tags={self.tags})>"
















































