"""Watch source files and re-run tests each time anything changes."""

import subprocess
import sys
from datetime import datetime as DateTime

from pinerylabs.watchers import Watcher

__all__ = []


########################################################################################################################

if __name__ == "__main__":
    runner = sys.argv[1]
    target_dir = sys.argv[2]

    def do_work(run_count: int):
        subprocess.run("clear")
        print(f"Starting test run {run_count} at {DateTime.now():%Y-%m-%d %H:%M}", flush=True)
        subprocess.run(f"{runner} run {target_dir}", shell=True)

    Watcher(sys.argv[2], do_work).start()
