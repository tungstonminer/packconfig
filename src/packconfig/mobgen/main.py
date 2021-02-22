"""Execute a sample config generation."""

import subprocess
import sys

from packconfig.mobgen.configs import brunel


########################################################################################################################

if __name__ == "__main__":
    target_dir = sys.argv[1]
    stdin_path = sys.argv[2]

    if target_dir == "ignore":
        target_dir = None

    brunel.config.generate(target_dir)

    if stdin_path != "ignore":
        subprocess.run(f"echo '/ctrlreload' >> {stdin_path}", shell=True)
        subprocess.run(f"echo '/ctrlkill all -1' >> {stdin_path}", shell=True)
        subprocess.run(f"echo '/ctrlkill all 0' >> {stdin_path}", shell=True)
        subprocess.run(f"echo '/ctrlkill all 1' >> {stdin_path}", shell=True)
