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

- @click.group() - Defines the main CLI group.
- menu() - Displays the main menu and handles user input for different operations.
- add() - Prompts the user for details of a new journal entry and adds it to the database.
- list_entries() - Lists all journal entries from the database.
- find_entries() - Prompts the user for a tag and displays entries matching that tag.
- update_entries() - prompts the user for an entry ID and new details, then updates the entry in the database.
- delete_entries() - prompts the user for an entry ID and deletes the corresponding entry
