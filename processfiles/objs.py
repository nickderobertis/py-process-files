import ast
import os
from typing import Iterable

from processfiles.filetools import write_to_file_with_retries, open_file_with_retries
from processfiles.timing import TimeTracker


class ObjectProcessTracker:

    def __init__(self, objs: Iterable, restart=False, completed_list_path: str = '_completed.txt'):
        self.completed_list_path = completed_list_path

        if restart:
            self.delete_completed_files()
        self.restart = restart
        self.objs = objs

        self.load_completed_files()

    def obj_generator(self):
        timer = TimeTracker(None, restart=self.restart)
        num_items = len(self.objs)

        for obj in self.objs:
            if self._has_been_completed(obj):
                continue
            yield obj
            self.add_to_completed(obj)
            timer.time_estimate(num_items)

        # time_estimate is end \r, so this cancels the next output from writing over the final time estimate
        print('\n')

    def add_to_completed(self, obj):
        self.completed_list.append(str(obj))
        _update_completed_files(self.completed_list_path, self.completed_list)

    def load_completed_files(self):
        self.completed_list = _load_completed_files(self.completed_list_path)

    def delete_completed_files(self):
        _delete_completed_files(self.completed_list_path)

    def _has_been_completed(self, obj):
        return str(obj) in self.completed_list


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