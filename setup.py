from setuptools import setup, find_packages

setup(
    name="tutor-mycustompages",
    version="0.1.4",
    packages=find_packages(),
    entry_points={
        "tutor.plugins.v1": [
            "mycustompages = tutor_mycustompages",
        ],
    },
)

