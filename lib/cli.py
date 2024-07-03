# lib/cli.py
#!/usr/bin/env python3

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()

# from models.__init__ import CONN, CURSOR
# from controllers import journal_controller

# def main():
#     while True:
#         journal_controller.menu()
#         choice = input("> ")
#         if choice == "0":
#             CONN.close()
#             break
#         elif choice == "1":
#             journal_controller.add_entry()
#         elif choice == "2":
#             journal_controller.get_all_entries()
#         elif choice == "3":
#             journal_controller.delete_entry()
#         elif choice == "4":
#             journal_controller.update_entry()
#         else:
#             print("Invalid choice")









import click
from datetime import datetime
from helpers import (
    create_table,
    add_entry,
    get_all_entries,
    find_entries_by_tag,
    delete_entry,
    update_entry
)
from models.journal_entry import JournalEntry

@click.group()
def cli():
    """Journal CLI"""
    create_table()

@cli.command()
def menu():
    """Display main menu"""
    while True:
        click.echo("\nPlease select an option:")
        click.echo("0. Exit")
        click.echo("1. Create a new journal entry")
        click.echo("2. List all journal entries")
        click.echo("3. Update a journal entry")
        click.echo("4. Search journal entries by tag")
        click.echo("5. Delete a journal entry")


        choice = click.prompt("Select an option", type=int)

        if choice == 0:
            click.echo("Exiting program. Goodbye!")
            break
        elif choice == 1:
            add()
        elif choice == 2:
            list_entries()
        elif choice == 3:
            update_entries()
        elif choice == 4:
            find_entries()
        elif choice == 5:
            delete_entries()

        else:
            click.echo("Invalid choice. Please select a valid option.")

def parse_tags(tags_str):
    """Convert a comma-separated string of tags into a list."""
    return [tag.strip() for tag in tags_str.split(',')]

def parse_date(date_str):
    """Convert a string into a datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise click.ClickException("Invalid date format. Use YYYY-MM-DD.")

def add():
    """Add a new journal entry"""
    title = click.prompt("Title", type=str)
    content = click.prompt("Content", type=str)
    tags_str = click.prompt("Tags (comma-separated)", type=str)
    date_str = click.prompt("Date (YYYY-MM-DD)", type=str)

    tags = parse_tags(tags_str)
    date = parse_date(date_str)

    entry = JournalEntry(None, title, content, tags, date)
    add_entry(entry)
    click.echo("Journal entry added successfully.")

def list_entries():
    """List all journal entries"""
    entries = get_all_entries()
    if entries:
        for entry in entries:
            click.echo(f"{entry}")
    else:
        click.echo("No journal entries found.")

def find_entries():
    """Prompt for tag to find entries"""
    tag = click.prompt("Enter tag to search", type=str)
    entries = find_entries_by_tag(tag)
    if entries:
        for entry in entries:
            click.echo(f"{entry}")
    else:
        click.echo(f"No entries found with tag '{tag}'.")

def delete_entries():
    """Prompt for entry ID to delete"""
    entry_id = click.prompt("Enter ID of the entry to delete", type=int)
    delete_entry(entry_id)
    click.echo(f"Journal entry {entry_id} deleted successfully.")

def update_entries():
    """Prompt for entry ID and new details to update"""
    entry_id = click.prompt("Enter ID of the entry to update", type=int)
    title = click.prompt("New Title", type=str)
    content = click.prompt("New Content", type=str)
    tags_str = click.prompt("New Tags (comma-separated)", type=str)
    date_str = click.prompt("New Date (YYYY-MM-DD)", type=str)

    tags = parse_tags(tags_str)
    date = parse_date(date_str)

    update_entry(entry_id, title, content, tags, date)
    click.echo(f"Journal entry {entry_id} updated successfully.")

if __name__ == "__main__":
    cli()














