"""Define a generation schema which matches the default ThermalFoundation oil config."""

from packconfig.oregen import ConfigFile


########################################################################################################################

config = ConfigFile(
    enabled=False,
    file_name="02_thermalfoundation_oil.json",
    priority=998,
)
