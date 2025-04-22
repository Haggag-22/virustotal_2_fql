from setuptools import setup, find_packages

setup(
    name="vt2fql",
    version="1.0.0",
    description="Generate CrowdStrike Falcon queries from VirusTotal IOCs",
    author="Omar Haggag",
    packages=find_packages(),
    install_requires=[
        "click",
        "vt-py",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "vt2fql=vt2fql.cli:main"
        ]
    },
    python_requires=">=3.8",
)