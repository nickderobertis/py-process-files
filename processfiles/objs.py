from typing import Iterable, Optional
import math

from processfiles.timing import TimeTracker
from processfiles.base import BaseProcessTracker
import itertools


class ObjectProcessTracker(BaseProcessTracker):

    def __init__(self, objs: Iterable, restart=False, completed_list_path: str = '_completed.txt'):
        self.completed_list_path = completed_list_path

        if restart:
            self.delete_completed_files()
        self.restart = restart
        self.objs = objs

        self.load_completed_files()

    def obj_generator(self, chunk: Optional[int] = None):
        timer = TimeTracker(None, restart=self.restart)
        num_items = len([obj for obj in self.objs if not self._has_been_completed(obj)])

        if chunk:
            num_items = math.ceil(num_items / chunk)
            for objs_chunk in chunk_generator(chunk, self.objs):
                valid_chunk = []
                for obj in objs_chunk:
                    if not self._has_been_completed(obj):
                        valid_chunk.append(obj)
                if not valid_chunk:
                    continue
                yield valid_chunk
                [self.add_to_completed(obj) for obj in valid_chunk]
                timer.time_estimate(num_items)
        else:
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


def chunk_generator(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk
