"""Define a generation schema which matches the default ThermalFoundation ore config."""

from packconfig.oregen import ConfigFile


########################################################################################################################

config = ConfigFile(
    enabled=False,
    file_name="01_thermalfoundation_ores.json",
    priority=999,
)
