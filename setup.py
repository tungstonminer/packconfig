"""Package definition."""

import setuptools

setuptools.setup(
    name="oregen",
    version="1.0.0",
    description="Code for generating TeamCOFH world generation files.",
    author="Andrew Miner",
    author_email="andrew@pinerylabs.com",

    packages=[
        "pinerylabs",
        "pinerylabs.oregen",
    ],
    package_dir={"": "src"},

    install_requires=[
    ],
)
