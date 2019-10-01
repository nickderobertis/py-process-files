import ast
import os
from typing import Iterable

from processfiles.filetools import write_to_file_with_retries, open_file_with_retries


class BaseProcessTracker:
    completed_list_path = None  # subclass needs to set this

    def add_to_completed(self, obj):
        self.completed_list.append(str(obj))
        _update_completed_files(self.completed_list_path, self.completed_list)

    def load_completed_files(self):
        self.completed_list = _load_completed_files(self.completed_list_path)

    def delete_completed_files(self):
        _delete_completed_files(self.completed_list_path)


def _update_completed_files(completed_list_path, completed_list):
    write_to_file_with_retries(completed_list_path, completed_list)


def _load_completed_files(completed_list_path):

    # Not started yet, none completed
    if not os.path.exists(completed_list_path):
        return []

    list_str = open_file_with_retries(completed_list_path)
    completed_list = ast.literal_eval(list_str)
    if not isinstance(completed_list, list):
        raise ValueError('completed list file contains other than list')

    return completed_list


def _delete_completed_files(completed_list_path):
    if os.path.exists(completed_list_path):
        os.remove(completed_list_path)