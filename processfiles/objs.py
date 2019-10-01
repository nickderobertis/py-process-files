from typing import Iterable

from processfiles.timing import TimeTracker
from processfiles.base import BaseProcessTracker


class ObjectProcessTracker(BaseProcessTracker):

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

    def _has_been_completed(self, obj):
        return str(obj) in self.completed_list
