from setuptools import setup, find_packages

setup(
    name="config_converter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "python-dotenv"
    ],
    tests_require=[
        "pytest"
    ],
    entry_points={
        "console_scripts": [
            "config_converter=config_converter.cli:main"
        ]
    }
)
