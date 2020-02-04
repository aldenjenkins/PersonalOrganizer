from typing import Iterable

from journal.models import JournalEntry
from todos.models import TodoEntry


def construct_digest_email_text(todo_entries: Iterable[TodoEntry],
                                journal_entries: Iterable[JournalEntry]) -> str:
    text = """Incomplete Todos:
{}

Unread Journals:
{}
    """.format(
        "\n".join([todo.text for todo in todo_entries]),
        "\n".join([journal.text for journal in journal_entries])
    )
    return text
