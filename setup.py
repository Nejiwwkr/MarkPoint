from setuptools import setup, find_packages

setup(
    name="markpoint",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'markpoint = markpoint.cli:main'
        ]
    }
)