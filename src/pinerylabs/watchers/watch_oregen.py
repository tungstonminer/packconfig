"""Watch source files and re-run generation each time anything changes."""

import subprocess
import sys
from datetime import datetime as DateTime

from pinerylabs.watchers import Watcher

__all__ = []


########################################################################################################################

if __name__ == "__main__":
    python = sys.argv[1]
    source_dir = sys.argv[2]
    target_path = sys.argv[3]
    stdin_path = sys.argv[4]

    def do_work(run_count: int):
        print(f"Starting generation run {run_count} at {DateTime.now():%Y-%m-%d %H:%M}")
        subprocess.run(f"{python} -m pinerylabs.oregen.main {target_path} {stdin_path}", shell=True)

    Watcher(source_dir, do_work, ["*.py"]).start()
