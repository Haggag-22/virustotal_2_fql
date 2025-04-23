from setuptools import setup, find_packages

setup(
    name="vt2fql",
    version="1.0.0",
    description="Generate Falcon FQL queries from VirusTotal IOCs",
    author="Omar Haggag",
    packages=find_packages(include=["backend", "backend.*"]),
    install_requires=[
        "click>=8.0,<9.0",
        "vt-py>=0.7,<1.0",
        "python-dotenv>=1.0,<2.0"
    ],
    entry_points={
        "console_scripts": [
            "vt2fql=backend.cli:main"
        ]
    },
    python_requires=">=3.8",
)