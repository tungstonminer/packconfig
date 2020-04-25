"""Watch source files and re-run tests each time anything changes."""

import time

from typing import Callable, List
from watchdog.events import FileSystemEvent, PatternMatchingEventHandler
from watchdog.observers import Observer

__all__ = []


########################################################################################################################

class DedupHandler(PatternMatchingEventHandler):

    def __init__(self, do_work: Callable, patterns: List[str] = None):
        patterns = patterns if patterns is not None else ["*.py"]
        super().__init__(patterns=patterns, ignore_directories=True)
        self.do_work = do_work
        self.run_count = 1

    def on_any_event(self, event: FileSystemEvent):
        if (event is not None) and (event.event_type != "created"):
            return

        self.do_work(self.run_count)
        self.run_count += 1


class Watcher(object):

    def __init__(self, target_dir: str, do_work: Callable, patterns: List[str] = None):
        self._handler = DedupHandler(do_work, patterns)
        self._observer = Observer()
        self._observer.schedule(self._handler, target_dir, recursive=True)

    def start(self):
        self._handler.on_any_event(None)
        self._observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self._observer.stop()

        self._observer.join()
