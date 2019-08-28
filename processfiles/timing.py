import os
import ast
import timeit
import datetime
from processfiles.filetools import write_to_file_with_retries, open_file_with_retries


class TimeTracker:
    """
    Tracks progress and displays estimated finish time.

    Usage:
    >>> timer = TimeTracker('outfolder')
    >>> items = [1, 2, 3]
    >>> for item in items:
    >>>     timer.time_estimate(len(items))
    """

    def __init__(self, folder, restart=False):

        if folder is None:
            self.folder = os.getcwd()
        else:
            self.folder = folder

        self.time_path = os.path.join(self.folder, 'time.txt')

        if restart:
            self.delete_previous_time()

        self.load_time()
        self.start_timer()

    def time_estimate(self, total_num_items):
        self._increment_time_and_items_completed()
        items_remaining = total_num_items - self.items_completed
        time_per_item = self.time / self.items_completed
        finish_time = datetime.datetime.now() + datetime.timedelta(seconds=items_remaining * time_per_item)
        print(f'Completed {self.items_completed}/{total_num_items} ({self.items_completed/total_num_items:.0%}) Estimated finish: {finish_time}', end='\r')

    def start_timer(self):
        self.start_time = timeit.default_timer()

    def load_time(self):
        self.original_time, self.items_completed = _load_time(self.time_path)
        self.time = self.original_time

    def _increment_time_and_items_completed(self):
        self.time = timeit.default_timer() - self.start_time + self.original_time
        self.items_completed += 1

    def save_time(self):
        _save_time(self.time_path, self.time, self.items_completed)

    def delete_previous_time(self):
        _delete_time_file(self.time_path)


def _delete_time_file(time_filepath):
    if os.path.exists(time_filepath):
        os.remove(time_filepath)


def _save_time(time_filepath, time, items_completed):
    time_dict = {
        'time': time,
        'items_completed': items_completed
    }

    write_to_file_with_retries(time_filepath, time_dict)


def _load_time(time_filepath):
    if not os.path.exists(time_filepath):
        return 0, 0

    time_str = open_file_with_retries(time_filepath)
    time_dict = ast.literal_eval(time_str)
    if not isinstance(time_dict, dict):
        raise ValueError('got other than dictionary in time file')

    return time_dict['time'], time_dict['items_completed']
