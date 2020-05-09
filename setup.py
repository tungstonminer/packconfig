"""Package definition."""

import setuptools

setuptools.setup(
    name="packconfig",
    version="1.0.0",
    description="A Python API for auto-generating config files for Minecraft modpacks.",
    author="Andrew Miner",
    author_email="andrewminer@mac..com",

    packages=[
        "packconfig",
        "packconfig.mobgen",
        "packconfig.mobgen.configs",
        "packconfig.oregen",
        "packconfig.oregen.configs",
        "packconfig.oregen.data",
        "packconfig.oregen.deposits",
        "packconfig.oregen.distributions",
        "packconfig.watchers",
    ],
    package_dir={"": "src"},

    install_requires=[
    ],
)
