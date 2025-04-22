from setuptools import setup, find_packages

setup(
    name="vt2fql",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "vt-py",
        "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'vt2fql=vt2fql.cli:main',
        ],
    },
    author="Omar Haggag",
    description="Generate FQL queries from VirusTotal IOCs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)