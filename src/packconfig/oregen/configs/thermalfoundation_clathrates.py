"""Define a generation schema which matches the default ThermalFoundation clathrates config."""

from packconfig.oregen import ConfigFile


########################################################################################################################

config = ConfigFile(
    enabled=False,
    file_name="03_thermalfoundation_clathrates.json",
    priority=997,
)
