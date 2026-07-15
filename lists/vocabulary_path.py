from pathlib import Path

from talon import Context, Module

mod = Module()
ctx = Context()

VOCABULARY_PATH = Path(__file__).parent / "vocabulary.talon-list"


@ctx.action_class("user")
class UserActions:
    def get_vocabulary_file_path():
        return str(VOCABULARY_PATH)
