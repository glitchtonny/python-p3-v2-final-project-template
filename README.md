# PERSON JOURNAL CLI APPLICATION

# Project Overview

This project is a Command-Line Interface (CLI) application for managing journal entries.
The application allows users to add, list, find, delete, and update journal entries.
Each journal entry can have multiple tags associated with it, establishing a one-to-many relationship between journal entries and tags.
The application uses SQLite for data storage.

## FEATURES

1. Add journal entries - Users can add new journal entries with a title, content, tags and date.
2. List journal entries - Users can list all journal entries
3. Find journal entries - Users can search all journal entries by specific tag
4. update journal entries - Users can update journal entries
5. Delete journal entries - Users can delete journal entries by its id

## FILES

# cli.py

This is the main entry point for the CLI application.it defines the commands available to the user and interact with the helpers function.

- **`create_table()`**: Creates the necessary tables (`journal_entries` and `tags`) in the database.
- **`add_entry(entry)`**: Adds a new journal entry and its associated tags to the database.
- **`get_all_entries()`**: Retrieves all journal entries along with their tags.
- **`find_entries_by_tag(tag)`**: Finds journal entries that match a specific tag.
- **`delete_entry(entry_id)`**: Deletes a journal entry by its ID.
- **`update_entry(entry_id, title, content, tags, date)`**: Updates an existing journal entry and its tags.

# helpers.py

This file contains helper functions for database operations. It interacts with the SQLite database to perform CRUD operations.

- **`create_table()`**: Creates the necessary tables (`journal_entries` and `tags`) in the database.
- **`add_entry(entry)`**: Adds a new journal entry and its associated tags to the database.
- **`get_all_entries()`**: Retrieves all journal entries along with their tags.
- **`find_entries_by_tag(tag)`**: Finds journal entries that match a specific tag.
- **`delete_entry(entry_id)`**: Deletes a journal entry by its ID.
- **`update_entry(entry_id, title, content, tags, date)`**: Updates an existing journal entry and its tags.

# Models/journal_entry.py

This file defines the JournalEntry class, which represents a journal entry.

- **`__init__(self, id, title, content, tags, date)`**: Initializes a new journal entry object.
- **`__repr__(self)`**: Returns a string representation of the journal entry object.

## instalation

1. Clone the repository
2. Install the required packages
   `pip install click`

3. Run the cli.py application

# Usage

## Add a New Journal Entry:

1. Select option 1 from the menu.
2. Enter the title, content, tags (comma-separated), and date (YYYY-MM-DD).

## List All Journal Entries:

1. Select option 2 from the menu.

## Find Journal Entries by Tag:

1. Select option 3 from the menu.
2. Enter the tag to search.

## Delete a Journal Entry:

1. Select option 4 from the menu.
2. Enter the ID of the entry to delete.

## Update a Journal Entry:

1. Select option 5 from the menu.
2. Enter the ID of the entry to update.
3. Enter the new title, content, tags (comma-separated), and date (YYYY-MM-DD).
