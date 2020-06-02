"""Execute a sample config generation."""

import subprocess
import sys

from packconfig.oregen.configs import (
    ad_astra,
    ad_astra_asteroids,
    # thermalfoundation_clathrates,
    # thermalfoundation_oil,
    # thermalfoundation_ores,
    vanilla,
)


########################################################################################################################

FILES = [
    ad_astra.config,
    ad_astra_asteroids.config,
    # thermalfoundation_clathrates.config,
    # thermalfoundation_oil.config,
    # thermalfoundation_ores.config,
    vanilla.config,
]


########################################################################################################################

if __name__ == "__main__":
    target_dir = sys.argv[1]
    stdin_path = sys.argv[2]

    for config_file in FILES:
        if target_dir == "ignore":
            config_file.print()
        else:
            config_file.write_file(target_dir)

    if stdin_path != "ignore":
        subprocess.run(f"echo '/cofhworld reload' >> {stdin_path}", shell=True)
